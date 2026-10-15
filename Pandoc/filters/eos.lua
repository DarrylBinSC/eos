--[[
eos.lua : Executive Operating System Pandoc filter (Pandoc 3.x)
Called by pandoc-watch.command after mermaid-filter. Rules are documented in Pandoc/README.md.

  1. Title promotion. If the file has no YAML title and opens with a level-1 heading,
     that heading becomes the document title (Title style plus the Word title property).
     If it was the only level-1 heading, every other heading moves up one level, so
     "##" sections become Heading 1. If other level-1 headings exist, levels are left
     alone. A file with neither gets its file name as the title, so the footer is never blank,
     and if it has no level-1 headings at all, its headings move up one level.
  2. Figures. An image standing alone in a paragraph (how Mermaid diagrams arrive) is
     centered and kept with what follows. If the next block is an "Image Caption" div,
     its text becomes the image's alt text.
  3. Table widths. When every column has the same relative width (Pandoc's result when
     the author did not size columns), widths are reset in proportion to the content.
     Tables the author sized deliberately, and short tables Pandoc autofits, are untouched.
]]

local stringify = pandoc.utils.stringify

-- 2. Figures ---------------------------------------------------------------
local function lone_image(b)
  return b.t == 'Para' and #b.content == 1 and b.content[1].t == 'Image'
end

local function is_caption_div(b)
  return b ~= nil and b.t == 'Div' and b.attributes['custom-style'] == 'Image Caption'
end

function Blocks(blocks)
  local out = pandoc.Blocks{}
  for i, b in ipairs(blocks) do
    if lone_image(b) then
      local img = b.content[1]
      local nxt = blocks[i + 1]
      if #img.caption == 0 and is_caption_div(nxt) then
        img.caption = pandoc.Inlines(stringify(nxt))
      end
      out:insert(pandoc.Div({ pandoc.Para{ img } }, { ['custom-style'] = 'Figure' }))
    else
      out:insert(b)
    end
  end
  return out
end

-- 3. Table widths ----------------------------------------------------------
local function ulen(s) return utf8.len(s) or #s end

local function longest_word(s)
  local m = 0
  for w in s:gmatch('%S+') do m = math.max(m, ulen(w)) end
  return m
end

function Table(tbl)
  local n = #tbl.colspecs
  if n < 2 then return nil end
  local w1 = tbl.colspecs[1][2]
  if type(w1) ~= 'number' then return nil end
  for i = 2, n do
    local w = tbl.colspecs[i][2]
    if type(w) ~= 'number' or math.abs(w - w1) > 0.001 then return nil end
  end

  local sum, cnt, head, hword = {}, {}, {}, {}
  for i = 1, n do sum[i], cnt[i], head[i], hword[i] = 0, 0, 0, 0 end
  local function scan(rows, is_head)
    for _, row in ipairs(rows) do
      local col = 1
      for _, cell in ipairs(row.cells) do
        local span = cell.col_span or 1
        if span == 1 and col <= n then
          local txt = stringify(cell.contents)
          if is_head then
            head[col] = math.max(head[col], ulen(txt))
            hword[col] = math.max(hword[col], longest_word(txt))
          else
            sum[col] = sum[col] + ulen(txt); cnt[col] = cnt[col] + 1
          end
        end
        col = col + span
      end
    end
  end
  scan(tbl.head.rows, true)
  for _, body in ipairs(tbl.bodies) do scan(body.body, false) end

  local weight, total = {}, 0
  for i = 1, n do
    local avg = cnt[i] > 0 and sum[i] / cnt[i] or 0
    weight[i] = math.min(math.max(avg, head[i] * 0.9, 4), 80)
    total = total + weight[i]
  end
  -- floor: no column narrower than 7% or than its longest header word
  local width, fixed = {}, 0
  for i = 1, n do
    local floor = math.max(0.07, hword[i] * 0.014 + 0.025)
    width[i] = math.max(weight[i] / total, floor)
    fixed = fixed + width[i]
  end
  for i = 1, n do
    tbl.colspecs[i] = { tbl.colspecs[i][1], width[i] / fixed }
  end
  return tbl
end

-- 1. Title promotion -------------------------------------------------------
local function title_from_filename()
  local f = PANDOC_STATE.input_files and PANDOC_STATE.input_files[1]
  if not f or f == '-' then return nil end
  local stem = (f:match('([^/\\]+)$') or f):gsub('%.[^.]+$', ''):gsub('_', ' ')
  return stem
end

function Pandoc(doc)
  if doc.meta.title ~= nil then return nil end
  local blocks = doc.blocks
  local first = blocks[1]
  if first and first.t == 'Header' and first.level == 1 then
    doc.meta.title = pandoc.MetaInlines(first.content)
    blocks:remove(1)
    local more_h1 = false
    for _, b in ipairs(blocks) do
      if b.t == 'Header' and b.level == 1 then more_h1 = true; break end
    end
    if not more_h1 then
      blocks = blocks:walk{ Header = function(h)
        if h.level > 1 then h.level = h.level - 1 end
        return h
      end }
    end
    doc.blocks = blocks
  else
    local t = title_from_filename()
    if t then doc.meta.title = pandoc.MetaInlines(pandoc.Inlines(t)) end
    local any_h1 = false
    for _, b in ipairs(blocks) do
      if b.t == 'Header' and b.level == 1 then any_h1 = true; break end
    end
    if not any_h1 then
      doc.blocks = blocks:walk{ Header = function(h)
        if h.level > 1 then h.level = h.level - 1 end
        return h
      end }
    end
  end
  return doc
end

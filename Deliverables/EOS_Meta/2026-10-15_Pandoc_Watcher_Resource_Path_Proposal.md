# Proposal: Pandoc watcher accepts image paths from the EOS root

As of: 2026-10-15. Status: **adopted 2026-10-15** at Darryl's direction and tested the same day (see `Pandoc/README.md`, change history). Decision: `03_Decision_Log.md`, 2026-10-15, item (7).

## What it fixes

The watcher runs Pandoc from the `Pandoc/` folder, and Pandoc resolves image paths from its working directory, not from the .md. An image written as `Deliverables/CDA/x.png` (the natural way to write it from the EOS root) does not resolve. Conversion still succeeds; the image is replaced by its description and the only signal is a warning in `Pandoc/output/<name>.log`. The `../Deliverables/...` form works today and is what the 2026-10-06 CDA exec brief used.

Verified 2026-10-15 with a test conversion: without the change, only the `../` path embedded; with it, both did.

## The change

1. Adds `--resource-path` covering `Pandoc/` first, then the EOS root. Both path forms work; nothing that works today breaks.
2. Prints a console warning when an image path does not resolve, instead of leaving it only in the log.
3. One banner line showing where image paths are resolved from.

No change to the template, the Lua filter, mermaid-filter or caption numbering.

## Diff

    --- Pandoc/pandoc-watch.command	2026-10-05 17:05:12.224592724 +0000
    +++ Deliverables/EOS_Meta/2026-10-15_pandoc-watch_PROPOSED.command	2026-10-15 11:09:52.854472619 +0000
    @@ -51,6 +51,14 @@
       LUA_ARGS=(-L "$LUA_FILTER")
     fi
     
    +# --- Image paths (proposed 2026-10-15) ----------------------------
    +# Pandoc resolves image paths from its working directory (this folder),
    +# not from the .md, so "Deliverables/..." paths used to fail silently.
    +# Searching this folder first, then the EOS root, accepts both
    +# "../Deliverables/..." (existing convention) and "Deliverables/...".
    +EOS_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
    +RESOURCE_PATH="$SCRIPT_DIR:$EOS_ROOT"
    +
     # --- Check pandoc is installed --------------------------------------
     if ! command -v pandoc >/dev/null 2>&1; then
       echo "ERROR: pandoc is not installed or not on your PATH."
    @@ -92,6 +100,7 @@
     else
       echo " Mermaid diagrams    : NOT rendered (install: npm install -g mermaid-filter)"
     fi
    +echo " Image paths from    : Pandoc/ and EOS root"
     echo " Checking every ${POLL_SECONDS}s.  Press Ctrl-C to stop."
     echo "=================================================="
     echo
    @@ -132,10 +141,14 @@
            ${filter_args[@]+"${filter_args[@]}"} \
            ${LUA_ARGS[@]+"${LUA_ARGS[@]}"} \
            ${toc_args[@]+"${toc_args[@]}"} \
    +       --resource-path="$RESOURCE_PATH" \
            -f markdown-tex_math_dollars \
            -t docx+native_numbering \
            -o "$OUTPUT/$name.docx" 2>"$OUTPUT/$name.log"; then
         echo "    -> $name.docx"
    +    if grep -q "Could not fetch resource" "$OUTPUT/$name.log" 2>/dev/null; then
    +      echo "    !! An image path did not resolve (see $name.log)"
    +    fi
         [ -s "$OUTPUT/$name.log" ] || rm -f "$OUTPUT/$name.log"
       else
         echo "    !! DOCX failed (see $name.log)"

The full proposed file is `Deliverables/EOS_Meta/2026-10-15_pandoc-watch_PROPOSED.command` (syntax-checked).

## To adopt

1. Stop the watcher (Ctrl-C or close its window).
2. Rename `Pandoc/pandoc-watch.command` to `Pandoc/SUPERSEDED_2026-10-15_pandoc-watch.command`.
3. Copy the proposed file into `Pandoc/` as `pandoc-watch.command`, and make it executable: `chmod +x pandoc-watch.command`.
4. Restart the watcher and confirm the banner shows "Image paths from".
5. Drop a test .md with one image in each path form into `inbox/`, and confirm both appear in the .docx.

Or tell Claude "adopt the watcher proposal" and Claude does steps 2, 3 and 5 and updates `Pandoc/README.md` and the "Markdown for the Word pipeline" rule; you only restart the watcher.

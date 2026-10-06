#!/bin/sh
# Validate the destination; Hugo owns file generation and YAML archetype expansion.
set -eu
kind=${1:?Content kind required}
: "${slug:?Use slug=a-lowercase-slug}"
: "${title:?Use title=Your title}"
case "$slug" in
  *[!a-z0-9-]*|-*|*-|'') echo 'slug must use lowercase ASCII letters, digits and internal hyphens' >&2; exit 2 ;;
esac
case "$title" in
  *[![:space:]]*) ;;
  *) echo 'title must not be blank' >&2; exit 2 ;;
esac
case "$kind" in
  note) target="notes/$slug" ;;
  post) target="blog/$(date +%Y)/$slug" ;;
  coding) target="coding/$slug" ;;
  page|draft) target="$slug" ;;
  *) echo 'Unknown content kind' >&2; exit 2 ;;
esac
# Reject even an empty existing bundle and symlink ancestors; never use --force.
path=content
oldIFS=$IFS
IFS=/
for part in $target; do
  path="$path/$part"
  if [ -L "$path" ]; then echo 'Destination contains a symlink' >&2; exit 2; fi
done
IFS=$oldIFS
if [ -L content ] || [ -e "content/$target" ]; then
  echo 'Destination already exists or content is a symlink; nothing overwritten' >&2
  exit 2
fi
export HUGO_NEW_TITLE="$title"
exec hugo new content --kind "$kind" "$target"

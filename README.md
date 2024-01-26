# Udacity Content Maintenance

Standardized formatting to propose content replacements.

## Folder Structure

- The pages are referenced by folders eg. `Course Title (shortened e.g. 'dpa') > Lesson Title > Page Title > Readme.md`.
- Each page directory is self contained. All the content and images are there.

## Page Formatting

- Please see the raw code of this document to understand the code.
- Each change is grouped in a collapsible section. Reasoning: They can be very long, so it's good to have a way to hide them when needed.
- Start with `Change #`.
- Use <span style="background: yellow">yellow highlights</span> to mark existing site content and <span style="background: lightgreen;"> lightgreen highlights</span> to wrap updated site content.
- **Ideally, all content inside green highlights can be copied directly into the editor.**

For example:

<details open>

<summary><b>Change 1:</b> Update this part of the content</summary>

Replace the this part:

<div style="background: yellow">

This is the part as exactly written on the page.

</div>

with the following:

<div style="background: lightgreen;">

This is the new **part**.

</div>

</details>

### Additional Notes

- `<div>` elements can be used to wrap paragraphs, but add a space before and after the Markdown content.
- Markdown is not supported inside `<summary>` tags so use HTMLs. For example, `<code>` tags can be used to emulate single backticks e.g.
    <details open>
    <summary><b>Change 1:</b> Both items in the numbered list are <code>1.</code>.</summary>
    </details>

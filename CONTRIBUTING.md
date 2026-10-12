# Contribution Guidelines

Do you want to get your work (article, plugin or other code) featured here?
Did you notice something missing, or a dead link?  
You're at the right place.

This list is not selective: anything YOURLS related gets listed, free or commercial.
Just make it clear to users what they are getting.

## Add or update an entry

**Do NOT edit `README.md`**: it is generated from the YAML files in [`data/`](https://github.com/YOURLS/awesome/tree/main/data).
Edit the file matching your content type instead:

| File | Content |
| --- | --- |
| `data/plugins.yml` | Plugins |
| `data/translations.yml` | Translations |
| `data/guides.yml` | Articles, tutorials, videos |
| ... |   |

Add your entry to the relevant file, following the existing format.  
For instance, for plugins:

```yaml
  - name: My Awesome Plugin
    url: https://github.com/you/yourls-awesome-plugin
    description: Concise and clear description explaining what your plugin does.
    category: security
    tags: [captcha, spam]
```

Tags are not rendered in the `README.md`, but they are used on the [interactive version](https://awesome.yourls.org/) to filter and search for content.

Refer to the top of each `.yml` file for details and help.

#### A few rules and tips:

* Pick the category that fits best. Unsure? Pick the closest one, we'll move it if needed.
* Keep the description to one line: what it does, not why it's great.
* Only direct and `https://` links.
* Host your resource somewhere users can interact with you (blog comments, Git aware site with issues
  or pull requests). This way, official YOURLS resources won't be polluted by questions about your
  material.

Open a pull request on the relevant `data/*.yml` file with your change: the `README.md` is regenerated
automatically, you don't need to run anything locally.

## Show off to your users

On your `README` or home page, let your users know you are listed here. The community grows faster
this way, and you will eventually get more users.

[![Listed in Awesome YOURLS!](https://img.shields.io/badge/Awesome-YOURLS-C5A3BE)](https://github.com/YOURLS/awesome-yourls/)

```
[![Listed in Awesome YOURLS!](https://img.shields.io/badge/Awesome-YOURLS-C5A3BE)](https://github.com/YOURLS/awesome-yourls/)
```

Append `?style=plastic`, `?style=flat-square` or `?style=flat` to the image URL for other
looks.

## Code of Conduct

This project is released with a
[Contributor Code of Conduct](https://github.com/YOURLS/.github/blob/master/CODE_OF_CONDUCT.md).
By participating, you agree to abide by its terms.

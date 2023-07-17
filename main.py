import os
import markdown

for article in os.listdir('articles'):

    file_input = article
    file_output = article.replace('.md', '.html')

    with open(f'articles/{file_input}', 'r') as f:
        content = f.read()

    output = markdown.markdown(content)

    html = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="style.css">
            <title>Document</title>
        </head>
        <body>
            <section class="container-md">
                {output}
            </section>
        </body>
        </html>
    '''

    with open(f'build/{file_output}', 'w') as f:
        f.write(html)

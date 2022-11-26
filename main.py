import shutil
import os 


def header():
    return f'''
        <header>
            <nav>
                <a href="#">
                    Martin Pellizzer
                </a>
                <ul>
                    <li>
                        <a href="#">Home</a>
                    </li>
                    <li>
                        <a href="#">Blog</a>
                    </li>
                    <li>
                        <a href="#">About</a>
                    </li>
                    <li>
                        <a href="#">Contact</a>
                    </li>
                </ul>
            </nav>
        </header>
    '''
def _main(filepath):
    return f'''
        <main>
            {article(filepath)}
            {aside()}
        </main>
    '''
def footer():

    return f'''
        <footer></footer>
    '''


def article(filepath):
    s = ''
    s += '<article>'
    with open(filepath) as f:
        content = f.read()
        s += content 
    s += '</article>'
    return s 
def aside():
    return f'''
        <aside>
            <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Voluptatem sapiente sed ipsam voluptate
                doloribus illum obcaecati ab distinctio autem optio sit, ex iure beatae, eveniet deleniti voluptates
                enim dignissimos quam.</p>
        </aside>
    '''


def body(filepath):
    return f'''
        {header()}
        {_main(filepath)}
        {footer()}
    '''

def html(filepath):
    return f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,500;1,600;1,700;1,800&display=swap" rel="stylesheet">
            <link rel="stylesheet" href="style.css">
            <title>Martin Pellizzer | Professional Home Lab</title>
        </head>
        <body>
            {body(filepath)}
        </body>
        </html>
    '''


def main():
    shutil.copy('style.css', './public/style.css')
    shutil.copy('CNAME', './public/CNAME')
    shutil.copy('./private/images/electronic-components.jpg', './public/electronic-components.jpg')

    article = 'index.html'
    with open(f'{article}', 'w') as f:
        content = f.read()
    with open(f'./public/{article}', 'w') as f:
        f.write(content)
        
    articles_folder = './private/articles/'
    for article in os.listdir(articles_folder):
        with open(f'./public/{article}', 'w') as f:
            f.write(html(f'{articles_folder}{article}'))

main() 
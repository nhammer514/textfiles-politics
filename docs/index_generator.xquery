<html>
    <head>
        <title>Full Text Links</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <link rel="stylesheet" href="CSSstyle.css"/>
    </head>
    <body>
        <button onclick="topFunction()" id="to-top" title="Go to top"><img alt="up arrow"
            src="https://cdn.onlinewebfonts.com/svg/img_231938.png" width="30" /></button>
        <h1 id="title-index">Full Text Links</h1>
        
        <nav id="menu">
            <a href="index.html"><div class="button">Home</div></a>
            <a href="fulltext.html"><div class="button">Fulltext</div></a>
            <a href="analysis.html"><div class="button">Analysis</div></a>
            <a href="gallery.html"><div class="button">Gallery</div></a>
            <a href="methods.html"><div class="button">Methods</div></a>
            <a href="about.html"><div class="button">About</div></a>
            <a href="GitHub.html"><div class="button">GitHub <img
                alt="github icon"
                src="https://logos-download.com/wp-content/uploads/2016/09/GitHub_logo.png"
                width="15" /></div></a>
                </nav>
            
        <h2>Conspiracy Directory</h2>
        <p> Thanks to Textfiles.com for their awesome archive of conspiracies!</p>
        <ol>
        {
        let $conspfiles := collection('../src-xml/')
        for $c in $conspfiles
            let $file := $c ! base-uri() ! tokenize(. , "/")[last()]
            let $htmlfile := $c ! base-uri() ! tokenize(., '/')[last()] ! substring-before(., '.xml')
            return <li><a href="collection/{$htmlfile}.html">{$file}</a></li>
        }
        </ol>
        <hr/>
        <h2 id="copyright">
            <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="GNU Public License e" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />
        </h2>
    </body>
</html>
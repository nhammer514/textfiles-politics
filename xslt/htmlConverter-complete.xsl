<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    xmlns="http://www.w3.org/1999/xhtml"
    exclude-result-prefixes="xs math"
    version="3.0">
    
   <xsl:output method="xhtml" html-version="5" omit-xml-declaration="yes" include-content-type="no" indent="yes"/>
    
    <!-- 2023-04-27 ebb:  This is XSLT Stage 2: Outputting HTML for the individual collection files -->
    <xsl:variable name="conspiracy" as="document-node()+" select="collection('../src-xml')"/>
    
    
    <xsl:template match="/">
        <xsl:for-each select="$conspiracy">   
            <xsl:variable name="filename" as="xs:string" select="current() ! base-uri() ! tokenize(., '/')[last()] ! substring-before(., '.xml')"/>
            <xsl:result-document method="xml" indent="yes" href="../docs/collection/{$filename}.html"> 
      <html>
            <head>
                <title><xsl:value-of select="$filename"/></title>
                <link rel="stylesheet" href="../CSSstyle.css"/>
                <!--Fill in your link line for CSS and JS in the XSLT here! -->
                <xsl:comment>Fill in your link line for CSS and JS in the XSLT here! </xsl:comment>   
            </head>
          <body>
              <h1 id="title-index"><xsl:value-of select="$filename"/></h1>
              <nav id="menu">
                  <a href="../index.html">
                      <div class="button">Home</div>
                  </a>
                  <a href="../fulltext.html">
                      <div class="button">Fulltext</div>
                  </a>
                  <a href="../analysis.html">
                      <div class="button">Analysis</div>
                  </a>
                  <a href="../gallery.html">
                      <div class="button">Gallery</div>
                  </a>
                  <a href="../methods.html">
                      <div class="button">Methods</div>
                  </a>
                  <a href="../about.html">
                      <div class="button">About</div>
                  </a>
                  <a href="../GitHub.html">
                      <div class="button">GitHub <img alt="github icon"
                          src="https://logos-download.com/wp-content/uploads/2016/09/GitHub_logo.png"
                          width="15"/>
                      </div>
                  </a>
              </nav>
               
               <xsl:apply-templates/>
            
            </body>
        </html>
            </xsl:result-document>
        </xsl:for-each>
       
 
    </xsl:template>
    
    <xsl:template match="p">
        <p>
            <xsl:apply-templates/>
        </p>
    </xsl:template>
    <!-- ebb: adding mouseover tooltip via title attribute-->
    <xsl:template match="ent">
        <span class="{@type}" title="{@type}">
            <xsl:apply-templates/>
        </span>
    </xsl:template>
    
    <!--ebb: What about the special and info XML tags? -->
    
    <xsl:template match="special">
        <span class="special">
            <xsl:apply-templates/>
        </span>
    </xsl:template>
  <xsl:template match="info">
      <span class="info" title="{@type}">
          <xsl:apply-templates/>
      </span>
    
  </xsl:template>
    
    
    
</xsl:stylesheet>
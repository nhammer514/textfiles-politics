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
            <xsl:result-document method="xml" indent="yes" href="../src-xml/{$filename}.html"> 
    =  <html>
            <head>
                <title><xsl:value-of select="$filename"/></title>
                <link/>
                <!--Fill in your link line for CSS and JS in the XSLT here! -->
                <xsl:comment>Fill in your link line for CSS and JS in the XSLT here! </xsl:comment>   
            </head>
          <body>
              <h1><xsl:value-of select="$filename"/></h1>
               
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
    
  
    
    
    
    
</xsl:stylesheet>
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    xmlns="http://www.w3.org/1999/xhtml"
    exclude-result-prefixes="xs math"
    version="3.0">
    
    <xsl:output method="xhtml" html-version="5" omit-xml-declaration="yes" 
        include-content-type="no" indent="yes"/>
    
    <xsl:template match="/">
        <html>
            <head>
                <title><xsl:value-of select="base-uri(.) ! tokenize(., '/')[last()] ! substring-before(., '.xml')"/></title>
                <link/>
                <!--Fill in your link line for CSS and JS in the XSLT here! -->
                <xsl:comment>Fill in your link line for CSS and JS in the XSLT here! </xsl:comment>
                
            </head>
            <body>
               
              <xsl:choose>
                  <xsl:when test="count(descendant::p) gt 1">
                      <div class="article"><xsl:apply-templates select=".//p" mode="multiparagraph"/></div>
                  </xsl:when>
                  <xsl:otherwise>
                      <xsl:apply-templates select=".//p"/>
                  </xsl:otherwise>
              </xsl:choose>
                
            </body>
        </html>
 
    </xsl:template>
    
    <xsl:template match="p" mode="multiparagraph">
        <p>
            <xsl:apply-templates/>
        </p>
    </xsl:template>
    
    <xsl:template match="p">
        <div class="article">
        <xsl:analyze-string select="." regex="(.+?)\n\n" flags="s">
            <xsl:matching-substring>
                <p><xsl:value-of select="regex-group(1)"/></p>
            </xsl:matching-substring>
            
         <!-- If we wanted to save the \n\n we could, but why?   <xsl:non-matching-substring>
                <xsl:value-of select="."/>
            </xsl:non-matching-substring>-->
        </xsl:analyze-string>
        </div>
    </xsl:template>
    
    
</xsl:stylesheet>
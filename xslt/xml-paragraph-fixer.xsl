<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    exclude-result-prefixes="xs math"
    version="3.0">
    
   <!-- <xsl:output method="xhtml" html-version="5" omit-xml-declaration="yes" 
        include-content-type="no" indent="yes"/>-->
    
    <!-- 2023-04-27 ebb:  This is XSLT Stage 1: fixing paragraphs in the XML.
    It is an XML-to-XML identity transformation, leaving the files intact but adding paragraph markup where it is missing.
    -->
    
    <xsl:variable name="conspiracy" as="document-node()+" select="collection('../regexConspTest')"/>
    
    <xsl:mode on-no-match="shallow-copy"/>
    
    <xsl:template match="/">
          <xml>

           <xsl:for-each select="$conspiracy">   
               <xsl:variable name="filename" as="xs:string" select="current() ! base-uri() ! tokenize(., '/')[last()]"/>
               <xsl:result-document method="xml" indent="yes" href="../src-xml/{$filename}"> 
                <!-- ebb: NEED TO LOOK UP HOW TO SET UP INDIVIDUAL RESULT DOCUMENTS output to folder  -->
               <xsl:choose>
                  <xsl:when test="count(descendant::p) gt 1">
                      <div class="article"><xsl:apply-templates select=".//p" mode="multiparagraph"/></div>
                  </xsl:when>
                  <xsl:otherwise>
                      <xsl:apply-templates select=".//p"/>
                  </xsl:otherwise>
              </xsl:choose>
               </xsl:result-document>
           </xsl:for-each>
        </xml>      
  
 
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
    
    <xsl:template match="info">
        <info type="{@type}">
            <xsl:apply-templates/>
        </info>
    </xsl:template>
    <xsl:template match="special">
        <info type="{@type}">
            <xsl:apply-templates/>
        </info>
    </xsl:template>
    
    
    
    
</xsl:stylesheet>
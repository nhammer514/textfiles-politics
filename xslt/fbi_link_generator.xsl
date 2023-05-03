<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    xpath-default-namespace="http://www.w3.org/2000/svg"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    exclude-result-prefixes="xs math"
    version="3.0">
    
   <!-- <xsl:output method="xhtml" html-version="5" omit-xml-declaration="yes" 
        include-content-type="no" indent="yes"/>-->
    
    <!-- 2023-04-27 ebb:  This is XSLT Stage 1: fixing paragraphs in the XML.
    It is an XML-to-XML identity transformation, leaving the files intact but adding paragraph markup where it is missing.
    -->
    
<!--    <xsl:variable name="conspiracy" as="document-node()+" select="doc('../docs/fbi-subnetwork.svg')"/>-->
    
    <xsl:mode on-no-match="shallow-copy"/>
    <xsl:template match="g[text[.!='North Korea' and .!='FBI']]">
        <xsl:copy>
            <xsl:apply-templates select="@*"/>
                <a xlink:href="collection/{text}.html#conspiracy" target="conspiracy">
                    
                    <xsl:apply-templates/>
                    
                </a>
                
        </xsl:copy>
        
    </xsl:template>
</xsl:stylesheet>
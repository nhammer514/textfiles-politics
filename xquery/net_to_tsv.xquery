xquery version "3.1";
        let $letStringJoin := string-join(
        let $conspiracyList := collection('../src-xml')//xml
        for $c in $conspiracyList
            let $names := $c//ent[@type='person']/text() => distinct-values()
            let $file := $c ! base-uri() ! tokenize(. , "/")[last()]
            for $n in $names
                return concat($n, "&#x9;", "person", "&#x9;", $file, "&#x9;", "file"),"&#10;"
                )
return $letStringJoin
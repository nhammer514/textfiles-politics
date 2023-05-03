var styles = [ {
  "format_version" : "1.0",
  "generated_by" : "cytoscape-3.9.1",
  "target_cytoscapejs_version" : "~2.1",
  "title" : "default",
  "style" : [ {
    "selector" : "node",
    "css" : {
      "shape" : "ellipse",
      "border-opacity" : 1.0,
      "background-opacity" : 1.0,
      "text-opacity" : 1.0,
      "height" : 35.0,
      "text-valign" : "center",
      "text-halign" : "center",
      "font-family" : "SansSerif.plain",
      "font-weight" : "normal",
      "color" : "rgb(247,252,245)",
      "border-color" : "rgb(204,204,204)",
      "background-color" : "rgb(137,208,245)",
      "width" : 35.0,
      "border-width" : 0.0,
      "font-size" : 12,
      "content" : "data(name)"
    }
  }, {
    "selector" : "node[Column_2 = '']",
    "css" : {
      "shape" : "rectangle"
    }
  }, {
    "selector" : "node[Column_2 = 'LOC']",
    "css" : {
      "shape" : "diamond"
    }
  }, {
    "selector" : "node[Column_2 = 'PERSON']",
    "css" : {
      "shape" : "triangle"
    }
  }, {
    "selector" : "node[Column_2 = 'ORG']",
    "css" : {
      "shape" : "diamond"
    }
  }, {
    "selector" : "node[Column_2 = 'NORP']",
    "css" : {
      "shape" : "diamond"
    }
  }, {
    "selector" : "node[Column_2 = 'GPE']",
    "css" : {
      "shape" : "diamond"
    }
  }, {
    "selector" : "node[Column_2 = 'EVENT']",
    "css" : {
      "shape" : "diamond"
    }
  }, {
    "selector" : "node[Column_2 = '']",
    "css" : {
      "background-color" : "rgb(12,44,132)"
    }
  }, {
    "selector" : "node[Column_2 = 'LOC']",
    "css" : {
      "background-color" : "rgb(217,240,163)"
    }
  }, {
    "selector" : "node[Column_2 = 'PERSON']",
    "css" : {
      "background-color" : "rgb(241,105,19)"
    }
  }, {
    "selector" : "node[Column_2 = 'ORG']",
    "css" : {
      "background-color" : "rgb(212,185,218)"
    }
  }, {
    "selector" : "node[Column_2 = 'NORP']",
    "css" : {
      "background-color" : "rgb(247,104,161)"
    }
  }, {
    "selector" : "node[Column_2 = 'GPE']",
    "css" : {
      "background-color" : "rgb(116,196,118)"
    }
  }, {
    "selector" : "node[Column_2 = 'EVENT']",
    "css" : {
      "background-color" : "rgb(227,26,28)"
    }
  }, {
    "selector" : "node[Column_2 = 'ORG']",
    "css" : {
      "color" : "rgb(37,37,37)"
    }
  }, {
    "selector" : "node:selected",
    "css" : {
      "background-color" : "rgb(255,255,0)"
    }
  }, {
    "selector" : "edge",
    "css" : {
      "color" : "rgb(0,0,0)",
      "line-style" : "solid",
      "font-family" : "Dialog.plain",
      "font-weight" : "normal",
      "target-arrow-color" : "rgb(0,0,0)",
      "font-size" : 10,
      "opacity" : 1.0,
      "width" : 2.0,
      "target-arrow-shape" : "none",
      "source-arrow-shape" : "none",
      "source-arrow-color" : "rgb(0,0,0)",
      "content" : "",
      "line-color" : "rgb(132,132,132)",
      "text-opacity" : 1.0
    }
  }, {
    "selector" : "edge[Column_4 > 381]",
    "css" : {
      "width" : 1.0
    }
  }, {
    "selector" : "edge[Column_4 = 381]",
    "css" : {
      "width" : 13.559900485403169
    }
  }, {
    "selector" : "edge[Column_4 > 1][Column_4 < 381]",
    "css" : {
      "width" : "mapData(Column_4,1,381,1.2611540817632907,13.559900485403169)"
    }
  }, {
    "selector" : "edge[Column_4 = 1]",
    "css" : {
      "width" : 1.2611540817632907
    }
  }, {
    "selector" : "edge[Column_4 < 1]",
    "css" : {
      "width" : 1.0
    }
  }, {
    "selector" : "edge[EdgeBetweenness > 2,422.45055709]",
    "css" : {
      "line-color" : "rgb(68,1,84)"
    }
  }, {
    "selector" : "edge[EdgeBetweenness = 2,422.45055709]",
    "css" : {
      "line-color" : "rgb(29,145,192)"
    }
  }, {
    "selector" : "edge[EdgeBetweenness > 2][EdgeBetweenness < 2,422.45055709]",
    "css" : {
      "line-color" : "mapData(EdgeBetweenness,2,2,422.45055709,rgb(253,187,132),rgb(29,145,192))"
    }
  }, {
    "selector" : "edge[EdgeBetweenness = 2]",
    "css" : {
      "line-color" : "rgb(253,187,132)"
    }
  }, {
    "selector" : "edge[EdgeBetweenness < 2]",
    "css" : {
      "line-color" : "rgb(253,231,37)"
    }
  }, {
    "selector" : "edge:selected",
    "css" : {
      "line-color" : "rgb(255,0,0)"
    }
  } ]
} ]
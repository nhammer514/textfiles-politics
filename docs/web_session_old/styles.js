var styles = [ {
  "format_version" : "1.0",
  "generated_by" : "cytoscape-3.9.1",
  "target_cytoscapejs_version" : "~2.1",
  "title" : "default",
  "style" : [ {
    "selector" : "node",
    "css" : {
      "color" : "rgb(255,255,255)",
      "width" : 35.0,
      "height" : 35.0,
      "background-color" : "rgb(33,113,181)",
      "font-family" : "SansSerif.plain",
      "font-weight" : "normal",
      "shape" : "roundrectangle",
      "background-opacity" : 1.0,
      "font-size" : 12,
      "border-opacity" : 1.0,
      "border-width" : 0.0,
      "text-valign" : "center",
      "text-halign" : "center",
      "border-color" : "rgb(204,204,204)",
      "text-opacity" : 1.0,
      "content" : "data(name)"
    }
  }, {
    "selector" : "node[Column_2 = 'person']",
    "css" : {
      "background-color" : "rgb(227,26,28)"
    }
  }, {
    "selector" : "node[Column_2 = 'person']",
    "css" : {
      "shape" : "diamond"
    }
  }, {
    "selector" : "node:selected",
    "css" : {
      "background-color" : "rgb(255,255,0)"
    }
  }, {
    "selector" : "edge",
    "css" : {
      "line-style" : "solid",
      "color" : "rgb(252,251,253)",
      "line-color" : "rgb(132,132,132)",
      "text-opacity" : 1.0,
      "source-arrow-color" : "rgb(0,0,0)",
      "target-arrow-color" : "rgb(0,0,0)",
      "font-family" : "Dialog.plain",
      "font-weight" : "normal",
      "content" : "",
      "font-size" : 10,
      "width" : 2.0,
      "source-arrow-shape" : "none",
      "opacity" : 1.0,
      "target-arrow-shape" : "none"
    }
  }, {
    "selector" : "edge[EdgeBetweenness > 2,826.99057424]",
    "css" : {
      "line-color" : "rgb(68,1,84)"
    }
  }, {
    "selector" : "edge[EdgeBetweenness = 2,826.99057424]",
    "css" : {
      "line-color" : "rgb(68,2,86)"
    }
  }, {
    "selector" : "edge[EdgeBetweenness > 1,414.49520293][EdgeBetweenness < 2,826.99057424]",
    "css" : {
      "line-color" : "mapData(EdgeBetweenness,1,414.49520293,2,826.99057424,rgb(33,145,140),rgb(68,2,86))"
    }
  }, {
    "selector" : "edge[EdgeBetweenness > 2][EdgeBetweenness < 1,414.49520293]",
    "css" : {
      "line-color" : "mapData(EdgeBetweenness,2,1,414.49520293,rgb(203,24,29),rgb(33,145,140))"
    }
  }, {
    "selector" : "edge[EdgeBetweenness = 2]",
    "css" : {
      "line-color" : "rgb(203,24,29)"
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
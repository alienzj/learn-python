#!/usr/bin/env python3

import pandas as pd
from plotnine import ggplot, aes, geom_point, theme_bw, xlab, ylab, ggtitle

midwest = pd.read_csv("http://goo.gl/G1K41K")
midwest = midwest[midwest.poptotal < 50000]

ggplot(
    aes(x="area", y="poptotal", color="state", size="popdensity"), data=midwest
) + geom_point() + theme_bw() + xlab("Area") + ylab("Population") + ggtitle(
    "Area vs Population"
)

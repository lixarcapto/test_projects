

import { Btjs } from "../../../btjs/Btjs.js";
import { ChartLegends } 
    from "../../btjs/mod/chart_legends/ChartLegends.js";

function main() {
    let legend = new ChartLegends()
    legend.to_document()
    legend.add_leyend("zona segura", "blue")
    legend.add_leyend("zonas no seguras", "green")
    legend.add_leyend("barrio rojo", "red")

}

main()
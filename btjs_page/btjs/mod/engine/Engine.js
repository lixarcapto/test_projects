
import { Btjs } 
    from "../../../btjs/Btjs.js";
import { Scenario } 
    from "../../../btjs/mod/scenario/Scenario.js";

export class Engine {

    constructor(width, height) {
        this.canvas = Btjs.Canvas(
            width, height)
        this.canvas.to_document()
        this.scenario = new Scenario()
        this.is_on = true
        this.frame_rate = 30
        this.frame_counter = 0
        this.final_frame_rate = 0
        this.scenario.set_size(width, height)
    }

    add_key_listener(KEY, CALLBACK) {
        this.canvas.add_key_listener(
            KEY, CALLBACK)
    }

    set_cam_location(point) {
        this.scenario.set_cam_location(point)
    }

    /*
    Asigna una url para la carpeta donde
    se almacenaran las imagenes a utilizar
    en los objetos.
    */
    set_folder_image_url(url_folder) {
        this.scenario.folder_resource_url
             = url_folder
    }

    /*
    Almacena una imagen de la carpeta
    de imagenes designada con una clave
    identificadora para utilizarla en
    los objetos como referencia.
    */
    set_image_in_folder(key, url_in_folder) {
        this.scenario.set_image_keyval(
            key,
            url_in_folder
        )
    }

    __draw_new_frame() {
        this.canvas.clear()
        let order_list = this.scenario
            .get_image_order_list()
        this.canvas.draw_image_order_list(
            order_list)
        this.canvas.draw_text(
            [
                this.canvas.size_x / 2 
                + this.canvas.size_x / 4,
                20
            ], 
            "FPS : " + String(
                this.final_frame_rate)
        )
        this.canvas.end_paint()
    }

    stop() {
        this.is_on = false
        this.scenario.stop()
    }

    start() {
        this.is_on = true
        this.scenario.start()
    }
    
    create_scenario() {
        this.scenario.create_scenario()
        console.log("framerate", 1 / this.frame_rate)
        Btjs.repeat_each(
            1 / this.frame_rate, 
                (n)=>{
            if( ! this.is_on) {return null}
            this.__draw_new_frame()
            this.frame_counter += 1
        })
        //contador de frames
        Btjs.repeat_each(1, 
                (n)=>{
            if(this.frame_counter) {
                this.final_frame_rate 
                    = this.frame_counter
                this.frame_counter = 0
            }
        })
    }

    set(gobject) {
        this.scenario.set(gobject)
    }

    get(id) {
        return this.scenario.get(id)
    }

    Gobject(id = "") {
        return this.scenario.Gobject(id)
    }

}
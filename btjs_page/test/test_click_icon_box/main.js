

import { Btjs } from "../../btjs/Btjs.js";

function main() {
    console.log("test_1")
    let icon_box = Btjs.ClickIconBox("iconos",
        ["perro", "gato", "raton"]
     )
     icon_box.to_document()
     let icon_url = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAIwSURBVGhD7ZhbcsMgEATB/76fj+j7+QDkQ0aG3WFfIMlJpauUSpDETvOQI6f0R8i04UAKbZiA5WYNC1kZXCLvPxZyVviW5SJ2ieeLtug87rSlEhKxh22JBJfopVSRWOgKCj8eVQ66v2IUmRNIIIRHoIX2UwEit6ahfJVE8t3bzshYgobzMAhTCi+XM1ogoL4wI7zX9O6AdjJJKQVKJOWcxg1KHCCQwCzknLtjhnaPfA1U2EJc5HH/HEZmR10iw6VFeb7kwNIyJPe1o03F6jnazvoXNruMJOGkDVk3d7vJmYSR29sodrcFOprNJqd/Qwl6/2BQ2xmpQj4xWsjBMHwAaWlRMb9kJSqr37dn8Yfa6B8QesEPg6Wxo/UFNnr3i5O4yAx8EPb80tL6VURF+pnkI7UepUZU5FywRDeYlj2if/JXjtgrWCLR7KMZKc1xHUaJNBC5NrwOk0hARJao7ykHva/M0NphiSsDO5aWLHKGBA1La9LzG0ORcyVwuA1UF18PH7/r/+XAxXVGtXl/7PG7XuIC6FPrCth6hygDfJZIFo4evoRM9CKK9ZfRbYlMG4Z4JQcvQAN4BlSPz9ber31pPXzfYTnRRFXsIpVjhT44a7RfB6FjjLOQAW+97nptRnShI6nhuQTDG3J6UxrgNTCuGaHogbjEEbAcXhGZNRIsJAGej4jAjgQJfL3MaG+itpSkEwLWNZyC/YeIzIiV0yRSsJg2I5E+p4kURSKRfv5B/ADNY6BAo2TzAQAAAABJRU5ErkJggg=="
     icon_box.set_content_array(
        [
            icon_url,
            icon_url,
            icon_url
        ]
     )
     icon_box.add_listener_to("raton", ()=>{
        console.log("si funciona lol")
     })

}

main()
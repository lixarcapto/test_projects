

import { request_post } 
    from "request_post.js";

function main() {
    console.log("init....")
    button = document.getElementById(
        "button")
    url = "http://127.0.0.1:5000/request"
    button.addEventListener('click', 
        function() {
            console.log("funciona")
            request_post(url, 
            {"mensaje":"funciona"},
            (e)=>{console.log(e)})
        }
    );
}

main()
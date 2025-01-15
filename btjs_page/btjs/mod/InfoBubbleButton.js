



export class InfoBubbleButton {

    constructor(title, text) {
        this.node = document
            .createElement("button")
        this.node.innerHTML = title
        this.node.setAttribute("display",
            "block")
        this.div = document
            .createElement("div")
        this.div.setAttribute("style",
            `display: none;`
        )
        this.node.append(this.div)
        this.div.innerHTML = text
        this.node.addEventListener(
            'mouseover', () => {
            this.div.style.display = 'block';
        });
        this.node.addEventListener(
            'mouseout', () => {
            this.div.style.display = 'none';
        });
    }

}
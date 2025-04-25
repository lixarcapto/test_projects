


export class Quote {

    constructor() {
        this.text = "not found quote"
        this.autor = "unknown"
        this.title = "no title"
        this.date = "s.f"
        this.recovery_date = ""
        this.url = ""
    }

    set_data(data) {
        if("text" in data) {
            this.text = data["text"]
        }
        if("autor" in data) {
            this.autor = data["autor"]
        }
        if("title" in data) {
            this.title = data["title"]
        }
        if("date" in data) {
            this.date = data["date"]
        }
        if("url" in data) {
            this.url = data["url"]
        }
        if("recovery_date" in data) {
            this.recovery_date = data[
                "recovery_date"]
        }
    }

    create_reference() {
        let element = document
            .createElement("li")
        element.innerHTML 
            = `${this.autor}(${this.date}). 
        <em>${this.title}</em>. Available in 
        <a href="${this.url}">${this.url}</a>
        `
        if(this.recovery_date != "") {
            element.innerHTML += `
            recovered the 
            ${this.recovery_date}
            `
        }
        return element
    }

    create_quote() {
        let element = document
            .createElement("a")
        element.setAttribute("href", this.url)
        element.setAttribute("style", 
            "text-decoration: none;")
        element.innerHTML = `
        <em>"${this.text}"</em>
        (${this.autor}, ${this.date})
        `
        return element.outerHTML
    }


}
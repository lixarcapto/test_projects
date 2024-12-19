



export class ProgressBar {

    constructor(title, range_arr) {
        this.node = document.createElement(
            "section")
        this.node.setAttribute("tag",
            "progress_bar")
        this.title = document.createElement(
            "label")
        this.range_arr = [0, 0]
        this.title.innerHTML = title
        this.bar = document.createElement(
            "progress")
        this.bar.setAttribute("style",
            `
                width: 300px;
                height: 20px;
                background-color: #000000;
                background-color: #4CAF50;
            `
        )
        this.set_range_arr([0, 100])
        this.bar.value = 0
        this.node.append(this.title)
        this.node.append(this.bar)
    }

    set_range_arr(range_arr) {
        this.range_arr = range_arr
        this.bar.setAttribute("min", 
            range_arr[0])
        this.bar.setAttribute("max", 
            range_arr[1])
    }

    reach_max() {
        let v = this.bar.value
        let max = this.range_arr[1]
        if(v >= max) { return true }
        return false
    }

    set_value(value) {
        this.bar.value = value
    }

    get_value() {
        return this.bar.value
    }

}
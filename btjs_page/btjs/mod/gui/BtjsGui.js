

import { DataTypes } 
    from "../data_types/DataTypes.js";
// GUI -----------------------------------

import { ListOl } from "./ListOl.js";
import { ListUl } from "./ListUl.js";
import { Selector } from "./Selector.js";
import { TextArea } from "./TextArea.js";
import { Button } from "./Button.js";
import { ColorSelector } from "./ColorSelector.js";
import { Body } from "./Body.js";
import { LabelArea } from "./LabelArea.js";
import { Link } from "./Link.js";
import { Quote } from "./Quote.js";
import { Article } from "./Article.js";
import { TitleBar } from "./TitleBar.js";
import { Card } from "./Card.js";
import { PageStructure } from "./PageStructure.js";
import { References } from "./References.js";
import { VideoFigure } from "./VideoFigure.js";
import {Image} from "./Image.js";
import { CheckBoxTicket } from "./CheckBoxTicket.js";
import { InputList } from "./InputList.js";
import { ClickIconBox } from "./ClickIconBox.js";
import { ClickTextBox } from "./ClickTextBox.js";
import { InputSlider } from "./InputSlider.js";
import { DataBar } from "./DataBar.js";
import { RadioButtonList } from "./RadioButtonList.js";
import { CommentBox } from "./CommentBox.js";
import { ButtonList } from "./ButtonList.js";
import { SwipperNumber } from "./SwipperNumber.js";
import { CheckButton } from "./CheckButton.js";
import { Canvas } from "./Canvas.js";
import { ScrollList } from "./ScrollList.js";
import { ChangeColorButton } from "./ChangeColorButton.js";
import {Book } from "./Book.js";
import { Gauge } from "./Gauge.js";
import { BookMenu } from "./BookMenu.js";
import { ButtonChest } from "./ButtonChest.js";
import { ClickIconText } from "./ClickIconText.js";
import { ClickIconTextOverlay } from "./ClickIconTextOverlay.js";
import { ClickIconOnly} from "./ClickIconOnly.js";
import { IconChart } from "./IconChart.js";
import { InputTxt } from "./InputTxt.js";
import {BarChart} from "./BarChart.js";
import { TextField } from "./TextField.js"; 
import { Table } from "./Table.js";
import { Sign } from "./Sign.js";
import { InnerStyle } from "./InnerStyle.js";
import {Label} from "./Label.js";
import { Frame } from "./Frame.js";
import { Dice } from "./Dice.js";
import { SwipperText } from "./SwipperText.js";
import { InputImage } 
  from "./InputImage.js";
import { dowload_with_blop } 
  from "./dowload_with_blop.js";

export class BtjsGui {

    static ClickIconText(title, url) {
        return new ClickIconText(title, url);
    }

    static ClickIconTextOverlay(title, url) {
        return new ClickIconTextOverlay(title, 
          url);
    }


    

  
    static Button(text = "") {
      return new Button(text)
    }

    static Sign(text, width, height) {
      return new Sign(text, width, height)
    }

    static Table(title) {
      return new Table(title)
    }

    static InputImage(title) {
      return new InputImage(title);
    }

    static IconChart(title) {
      return new IconChart(title)
    }

    static InnerStyle(class_code, 
        pseudoclass = "") {
      return new InnerStyle(class_code, 
          pseudoclass)
    }

    static InputTxt(title) {
      return new InputTxt(title)
    }

    static Dice(size_x, size_y) {
      return new Dice(size_x, size_y)
    }

    static TextField(title) {
      return new TextField(title)
    }

    static BarChart(title) {
      return new BarChart(title)
    }

    static ClickIconOnly(title, url) {
      return new ClickIconOnly(title, url)
    }

    static BookMenu(text = "") {
      return new BookMenu(text)
    }

    static jump(number = 1) {
      let e = null
      for(let i=0;i< number; i++) {
        e = document.createElement("br")
        document.body.append(e)
      }
    }

    static to_body(widget_btjs) {
      document.body.append(widget_btjs.node)
    }

    static ListOl(text, ARRAY) {
      return new ListOl(text, ARRAY)
  }

  static ListUl(text, ARRAY) {
    return new ListUl(text, ARRAY)
}

    static LabelArea(text = "") {
      return new LabelArea(text)
    }

    static Gauge(text = "") {
      return new Gauge(text)
    }

    static Selector(text, ARRAY = []) {
      return new Selector(text, 
        ARRAY)
    }
    
    static Frame() {
      return new Frame()
    }
    
    static ButtonChest(title) {
      return new ButtonChest(title)
    }

    static Book() {
      return new Book()
    }

    static TextArea(key, text) {
      return new TextArea(key, text)
    }

    static color_selector() {
      return new ColorSelector()
    }

    static ChangeColorButton(text) {
      return new ChangeColorButton(text)
    }

    static StyleHead() {
      return new Body()
    }

    static Link(text, url) {
      return new Link(text, url)
    }

    static Quote() {
      return new Quote()
    }

    static Article(title, text = "", 
        level = 0) {
      return new Article(title, 
        text, level)
    }

    static Card(title, src, 
      description = "") {
        return new Card(title,
          src, description)
    }

    static TitleBar(title) {
      return new TitleBar(title)
    }

    static PageStructure() {
      return new PageStructure()
    }

    static References() {
      return new References()
    }

    static VideoFigure() {
      return new VideoFigure()
    }

    static Label(text = "") {
      return new Label(text)
    }

    static Image(url) {
      return new Image(url)
    }

    static CheckBoxTicket(title, text_arr) {
      return new CheckBoxTicket(title, text_arr)
    }

    static InputList(text_arr) {
      return new InputList(text_arr)
    }

    static ClickTextBox(title, key_arr) {
      return new ClickTextBox(title,
         key_arr)
    }

    static ClickIconBox(title, key_arr) {
      return new ClickIconBox(title,
         key_arr)
    }

    static InputSlider(title, range_arr, 
          value) {
      return new InputSlider(title, 
          range_arr, value)
    }

    static DataBar(title) {
      return new DataBar(title)
    }

    

    static RadioButtonList(title, text_arr) {
      return new RadioButtonList(title, 
          text_arr)
    }

    static CommentBox(json_arr = []) {
      return new CommentBox(json_arr)
    }

    static ButtonList(title, text_arr) {
      return new ButtonList(title, text_arr)
    }

    static IconButton(image_url, text) {
      return new IconButton(image_url, text)
    }

    static SwipperNumber(name, range_arr) {
      return new SwipperNumber(name, 
        range_arr)
    }

    static SwipperText(name, content_array) {
      return new SwipperText(
        name, content_array)
    }

    static CircleButton(title) {
      return new CheckButton(title, 
        "radio")
    }

    static CheckButton(title) {
      return new CheckButton(title, 
        "checkbox")
    }

    static Canvas(size_x, size_y) {
      return new Canvas(size_x, size_y)
    }

    static ScrollList(text_arr, height) {
      return new ScrollList(text_arr, height)
    }

    static dowload_with_blop(content) {
      return dowload_with_blop(content)
    }

}
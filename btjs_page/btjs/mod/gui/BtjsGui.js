

import { BtjsConverters } from "../converters/BtjsConverters.js";

// Labels -------------------------------
import { Label } from "./mod/Label.js";
import { Image } from "./mod/Image.js";
import { LabelArea } from "./mod/LabelArea.js";
import { LabelLabel } from "./mod/LabelLabel.js";

// Containers ----------------------------
import { Frame } from "./mod/Frame.js";

// Cards --------------------------------
import { Card } from "./mod/Card.js";

// Input Text
import { TextField } from "./mod/TextField.js";
import { TextArea } from "./mod/TextArea.js";

// Click Buttons ------------------------
import { ButtonIcon } from "./mod/ButtonIcon.js";
import {ButtonIconText} from "./mod/ButtonIconText.js";
import {ButtonIconTextOverlay} from "./mod/ButtonIconTextOverlay.js";
import { Button } from "./mod/Button.js";
import { Link } from "./mod/Link.js";

// Switch Buttons ------------------------
import { SwitchColor } from "./mod/SwitchColor.js";
import { SwitchCheck } from "./mod/SwitchCheck.js";

// Others -------------------------------
import { ColorSelector } from "./mod/ColorSelector.js";

// Swipers ------------------------------
import { SwiperRange } from "./mod/SwiperRange.js";
import { SwiperText } from "./mod/SwiperText.js";

// Boxes --------------------------------
import {RadioBoxClasic} from "./mod/RadioBoxClasic.js";
import { CheckBoxClasic } from "./mod/CheckBoxClasic.js";

export class BtjsGui extends BtjsConverters {

    // Labels ----------------------------

    static Label(TITLE_STR = "") {
      return new Label(TITLE_STR)
    }

    static LabelArea(TITLE_STR = "") {
      return new LabelArea(TITLE_STR)
    }

    static Image(IMAGE_URL_STR = "") {
      return new Image(IMAGE_URL_STR)
    }

    static LabelLabel(TITLE_STR,
        CONTENT_STR) {
      return new LabelLabel(TITLE_STR,
          CONTENT_STR)
    }

    //-----------------------------------

    // Click Buttons --------------------

    static Button(TITLE_STR = "") {
      return new Button(TITLE_STR)
    }
  
    static Link(TITLE_STR, URL_STR) {
      return new Link(TITLE_STR, URL_STR)
    }

    static ButtonIcon(TITLE_STR,
        IMAGE_URL_STR) {
      return new ButtonIcon(
        TITLE_STR,
        IMAGE_URL_STR
      )
    }

    static ButtonIconText(TITLE_STR,
        IMAGE_URL_STR) {
      return new ButtonIconText(
        TITLE_STR,
        IMAGE_URL_STR
      )
    }

    static ButtonIconTextOverlay(
        TITLE_STR,
        IMAGE_URL_STR) {
      return new ButtonIconTextOverlay(
        TITLE_STR,
        IMAGE_URL_STR
      )
    }

    // -----------------------------------

    // Input Text ------------------------

    static TextField(TITLE) {
      return new TextField(TITLE)
    }

    static TextArea(TITLE_STR, 
         TEXT_STR = "") {
      return new TextArea(TITLE_STR, 
        TEXT_STR)
    }

    // -----------------------------------

    // Containers ------------------------

    static Frame(TITLE_STR) {
      return new Frame(TITLE_STR)
    }

    // ---------------------------------

    // Cards ---------------------------

    static Card(TITLE_STR) {
      return new Card(TITLE_STR)
    }

    // ----------------------------------

    // Switch ---------------------------

    static SwitchCheck(TITLE_STR) {
      return new SwitchCheck(TITLE_STR)
    }

    static SwitchColor(TITLE_STR) {
      return new SwitchColor(TITLE_STR)
    }

    // ----------------------------------

    // Others ---------------------------

    static ColorSelector() {
      return new ColorSelector()
    }

    // ----------------------------------

    // Swipers --------------------------

    static SwiperRange(TITLE_STR,
        RANGE_LIST_X2) {
      return new SwiperRange(
        TITLE_STR,
        RANGE_LIST_X2
      )
    }

    static SwiperText(TITLE_STR, 
        CONTENT_LIST_STR) {
      return new SwiperText(TITLE_STR, 
        CONTENT_LIST_STR)
    }

    // ----------------------------------

    // Boxes ----------------------------

    static RadioBoxClasic(title, list) {
        return new RadioBoxClasic(
          title, list
        )
    }

    static CheckBoxClasic(title, list) {
        return new CheckBoxClasic(
            title, list
        )
    }

    // ----------------------------------

}
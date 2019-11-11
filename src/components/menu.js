import React, { Component } from "react";
import { Menu, Item, Separator, Submenu} from 'react-contexify';
import 'react-contexify/dist/ReactContexify.min.css';
import refreshComment from "../App"
import axios from 'axios';

//
//export default class CommentForm extends Component {
//    constructor(props) {
//        super(props);
//        this.state = {
//          loading: false,
//          error: "",
//
//          comment: {
//            name: "",
//            message: ""
//          }
//        };
//
//        // bind context to methods
//        this.delete1 = this.delete1.bind(this);
//        this.onClick = this.onClick.bind(this);
//
//        console.log('in constructor',this.props);
//    }
//
//    delete1 ()
//    {
//
//        console.log('in delete 1',this.props);
//        var time = this.props.ref.children[1].children[0].innerHTML
//        var name = this.props.ref.children[1].children[1].innerHTML
//        var comment = this.props.ref.children[1].children[2].innerHTML
//        var req = {"param": [name,comment]};
//        var strreq = JSON.stringify(req)
//        console.log(req, strreq);
//        fetch("http://localhost:7777", {
//          method: "delete",
//          body: strreq
//        })
//        .then(res=>res.json())
//        .then(res => {
//            console.log('props',this.props);
//    //        refreshComment();
//            console.log(res);
//        })
//    }
//
//    onClick(e) {
//    console.log('on click', this.props);
//    }
//
//    render () {
//        return(
//            <Menu id='menu_id'>
//               <Item onClick={this.delete1}>Delete</Item>
//               <Separator />
//               <Submenu label="Help">
//                <Item onClick={this.onClick}>Help 1</Item>
//                <Item onClick={this.onClick}>Help 2</Item>
//               </Submenu>
//            </Menu>
//        );
//    }
//}

export default function MyAwesomeMenu(props) {
  const onClick = ({ event, props }) => console.log('log',event,props);
  function delete1({props})
  {
    console.log(props)
    var time = props.ref.children[1].children[0].innerHTML
    var name = props.ref.children[1].children[1].innerHTML
    var comment = props.ref.children[1].children[2].innerHTML
    var req = {"param": [name,comment]};
    var strreq = JSON.stringify(req)
    console.log(req, strreq);
    fetch("http://localhost:7777", {
      method: "delete",
      body: strreq
    })
    .then(res=>res.json())
    .then(res => {
        console.log('props',props);
//        refreshComment();
        console.log(res);

          // TODO: remove
        window.location.reload();
    })

  }
return(
    <Menu id='menu_id'>
       <Item onClick={delete1}>Delete</Item>
       <Separator />
       <Submenu label="Help">
        <Item onClick={onClick}>Help 1</Item>
        <Item onClick={onClick}>Help 2</Item>
       </Submenu>
    </Menu>
);
}

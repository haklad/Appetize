import React, { Component } from "react";
import logo from "./logo.jpeg";
import "bootstrap/dist/css/bootstrap.css";
import "./App.css";

import { Menu, Item, Separator, Submenu} from 'react-contexify';

import CommentList from "./components/CommentList";
import CommentForm from "./components/CommentForm";
import MyAwesomeMenu from "./components/menu"
import { MenuProvider } from 'react-contexify';
import 'react-contexify/dist/ReactContexify.min.css';


//function MyAwesomeMenu(props) {
//  const onClick = ({ event, props }) => console.log('log',event,props);
//  function delete1({props})
//  {
//    console.log(props)
//    var time = props.ref.children[1].children[0].innerHTML
//    var name = props.ref.children[1].children[1].innerHTML
//    var comment = props.ref.children[1].children[2].innerHTML
//    var req = {"param": [name,comment]};
//    var strreq = JSON.stringify(req)
//    console.log(req, strreq);
//    fetch("http://localhost:7777", {
//      method: "delete",
//      body: strreq
//    })
//    .then(res=>res.json())
//    .then(res => {
//        console.log('props',props);
////        refreshComment();
//        console.log(res);
////        window.location.reload();
//    })
//
//  }
//return(
//    <Menu id='menu_id'>
//       <Item onClick={delete1}>Delete</Item>
//       <Separator />
//       <Submenu label="Help">
//        <Item onClick={onClick}>Help 1</Item>
//        <Item onClick={onClick}>Help 2</Item>
//       </Submenu>
//    </Menu>
//);
//}



class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      comments: [],
      loading: false
    };

    this.addComment = this.addComment.bind(this);
  }

  componentDidMount() {
    // loading
    this.setState({ loading: true });

    // get all the comments
    fetch("http://localhost:7777")
      .then(res => res.json())
      .then(res => {
        this.setState({
          comments: res,
          loading: false
        });
      })
      .catch(err => {
        this.setState({ loading: false });
      });
  }

  componentDidUpdate() {
  // only update chart if the data has changed
  //this.setState({ loading: true });
  console.log("update");
  // get all the comments
  // fetch("http://localhost:7777")
  //   .then(res => res.json())
  //   .then(res => {
  //     this.setState({
  //       comments: res,
  //       loading: false
  //     });
  //   })
  //   .catch(err => {
  //     this.setState({ loading: false });
  //   });
}

  /**
   * Add new comment
   * @param {Object} comment
   */
  addComment(comment) {
    this.setState({
      loading: false,
      comments: [comment, ...this.state.comments]
    });
  }


  refreshComment()
  {
    this.setState({
      loading: false,
      comments: [...this.state.comments]
    });
  }

  render() {
    const loadingSpin = this.state.loading ? "App-logo Spin" : "App-logo";
    return (
      <div className="App container bg-light shadow">
      <MyAwesomeMenu s={this.state} />
        <header className="App-header">
        <div className = "row">
              <div className="col-sm-6 image-container">
                <img src={logo} style={{"height":'200px', "marginLeft":'-15px'}} />
              </div>
              <div className="col-sm-6">
                <h3>Toscano</h3>
                 <p>Koramangala 7th Block   ·  Casual Dining Opening hours · Open now
Today  12noon – 11pm
See more
Happy Hours: # Monday To Friday 4 Pm To 8 Pm Enjoy Selected Beverages A Flat Price of 199/- # Buy a pitcher of Sangria/Mojito or a Beer Bucket & Get A Pizza Free* Buy 1 Get 1 on Sangria and Select Cocktails: All day everyday! # 50% off on all pizza Mon-Wed
Address
2nd Floor, Forum Mall, Koramangala 7th Block, Bangalore</p>
              </div>
            </div>
          </header>
        <div className="row">
          <div className="col-4 pt-3 border border-white rounded ">
            <h6>Say something about Toscano</h6>
            <CommentForm addComment={this.addComment} />
          </div>
          <div className="col-8  pt-3">
            <CommentList
              loading={this.state.loading}
              comments={this.state.comments}
            />
          </div>
        </div>
        </div>

    );
  }
}

export default App;

import React from "react";
import { MenuProvider } from 'react-contexify';
import MyAwesomeMenu from "./menu"

//export default function Comment(props) {
//  const { name, message, time } = props.comment;
//
//  return (
//  <MenuProvider id="menu_id">
//    <div className="media mb-3">
//      <img
//        className="mr-3 bg-light rounded"
//        width="48"
//        height="48"
//        src={`https://api.adorable.io/avatars/48/${name.toLowerCase()}@adorable.io.png`}
//        alt={name}
//      />
//
//      <div className="media-body p-2 shadow-sm rounded bg-light border">
//        <small className="float-right text-muted">{time}</small>
//        <h6 className="mt-0 mb-1 text-muted">{name}</h6>
//        <div>{message}</div>
//      </div>
//      </div>
//
//      </MenuProvider>
//  );
//}


export default function Comment(props) {
  const { name, message } = props.comment;

  return (
  <MenuProvider id="menu_id">
    <div className="media mb-3">
      <img
        className="mr-3 bg-light rounded"
        width="48"
        height="48"
        src={`https://api.adorable.io/avatars/48/${name.toLowerCase()}@adorable.io.png`}
        alt={name}
      />

      <div className="media-body p-2 shadow-sm rounded bg-light border">
        <h6 className="mt-0 mb-1 text-muted">{name}</h6>
        <div>{message}</div>
      </div>
      </div>

      </MenuProvider>
  );
}

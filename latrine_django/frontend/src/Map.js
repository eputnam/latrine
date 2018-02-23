import React, { Component } from 'react';
import './Map.css';

export default class Map extends React.Component {
  componentDidMount() {
    let map = new window.google.maps.Map(document.getElementById('map'), {
      center: {lat: 45.5221418, lng: -122.6776808},
      zoom: 13,
      mapTypeId: 'roadmap',
    });
  }
  render() {
    return (
      <div id='map' />
    );
  }
}

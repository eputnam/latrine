import React, { Component } from 'react';
import axios from 'axios';
import './Map.css';

export default class Map extends React.Component {

  constructor() {
    super()
    this.state = {
      restrooms: null,
    }
  }

  componentDidMount() {
    let map = new window.google.maps.Map(document.getElementById('map'), {
      center: {lat: 45.5221418, lng: -122.6776808},
      zoom: 13,
      mapTypeId: 'roadmap',
    });

    // Calling RefugeRestrooms API
    axios.get('https://www.refugerestrooms.org:443/api/v1/restrooms/by_location.json?lat=45.5221418&lng=-122.677680')
    .then((response) => {
      console.log(response.data);
      this.setState({ restrooms: JSON.stringify(response.data) });
    })
    .catch((error) => {
      console.log(error);
    });
  }

  render() {
    return (
      <div id='map' />
    );
  }
}

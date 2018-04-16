import React, { Component } from 'react';
import axios from 'axios';
import {Map, Marker, GoogleApiWrapper} from 'google-maps-react';
import './Map.css';


export class MapContainer extends Component {

  constructor() {
    super()
    this.state = {
      restrooms: [],
    }
  }

  componentDidMount() {
    // Calling RefugeRestrooms.org API
    axios.get('https://www.refugerestrooms.org:443/api/v1/restrooms/search.json?per_page=100&query=portland')
    .then((response) => {
      console.log(response.data);
      this.setState({ restrooms: response.data });
    })
    .catch((error) => {
      console.log(error);
    });
  }

  render() {
    return (
      <Map
      google={this.props.google}
      style={{width: '100%', height: '100%', margin: 'auto'}}
      containerStyle={{width: '100vw', height: '93vh', margin: 'auto'}}
      zoom={14}
      initialCenter={{
        lat: 45.5231,
        lng: -122.6765
      }}
      >
        {
          this.state.restrooms.map((i, markerindex) => {
            const google = window.google;
            if (this.props.restroomsChecked) {
            return (
              <Marker
              key={markerindex}
              title={'RefugeRestrooms.org -' + i.street}
              name={'RefugeRestrooms.org'}
              position={{ lat: i.latitude, lng: i.longitude }}
              icon={{
                url: require("./images/potty.png"),
                anchor: new google.maps.Point(32,32),
                scaledSize: new google.maps.Size(45,45)
              }}
              />
            )} else {
              return null
            }
          })
        }
      </Map>
    );
  }
}

export default GoogleApiWrapper({
  apiKey: ('AIzaSyCxZwna2Pr9JMOm1mUZC1iSMjiWaegroHo'),
  version: '3.31'
})(MapContainer)

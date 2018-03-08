import React, { Component } from 'react';
import MapContainer from './Map.js'
import './App.css';

export default class App extends Component {

  render() {
    return (
      <div className="app">
        <MapContainer />
      </div>
    );
  }
}

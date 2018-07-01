import React, { Component } from 'react';
import Drawer from '@material-ui/core/Drawer';
import MapContainer from './Map.js';
import Filters from './Filters.js';
import './App.css';

export default class App extends Component {
    constructor() {
        super();
        this.state = {
            restroomsChecked: true,
            drawer: false,
        };

        this.toggleRestrooms = this.toggleRestrooms.bind(this);
        this.toggleDrawer = this.toggleDrawer.bind(this);
    }

    toggleDrawer = isOpen => () => {
        this.setState({
            drawer: isOpen,
        });
    };

    toggleRestrooms() {
        this.setState({
            restroomsChecked: !this.state.restroomsChecked,
        });
    }

    render() {
        return (
            <div className="app">
                <Drawer
                    open={this.state.drawer}
                    onClose={this.toggleDrawer(false)}
                >
                    <div
                        tabIndex={0}
                        role="button"
                        onClick={this.toggleDrawer(false)}
                        onKeyDown={this.toggleDrawer(false)}
                    >
                        TEST
                    </div>
                </Drawer>
                <Filters
                    restroomsChecked={this.state.restroomsChecked}
                    toggleRestrooms={this.toggleRestrooms}
                    toggleDrawer={this.toggleDrawer}
                />
                <MapContainer restroomsChecked={this.state.restroomsChecked} />
            </div>
        );
    }
}

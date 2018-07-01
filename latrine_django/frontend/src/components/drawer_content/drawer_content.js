import React from 'react';

export default class DrawerContent extends React.Component {
    constructor() {
        super();

        this.makeListItems = this.makeListItems.bind(this);
    }

    makeListItems() {
        const {
            selectedRestroomData: { name, comment, street, city, country },
        } = this.props;
        //
        //Sidebar displays the Resources and Place information including photo, address, phone, comments, etc.
        //
        return (
            <React.Fragment>
                <li>{name}</li>
                <li>{comment}</li>
                <li>{street}</li>
                <li>{city}</li>
                <li>{country}</li>
            </React.Fragment>
        );
    }

    render() {
        return <ul>{this.makeListItems()}</ul>;
    }
}

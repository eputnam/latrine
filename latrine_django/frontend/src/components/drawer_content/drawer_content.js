import React from 'react';

export default class DrawerContent extends React.Component {
    render() {
        const {
            selectedRestroomData: { name, comment, street, city, country },
        } = this.props;

        //
        //Sidebar displays the Resources and Place information including photo, address, phone, comments, etc.
        //

        return (
            <ul>
                <li>{name}</li>
                <li>{comment}</li>
                <li>{street}</li>
                <li>{city}</li>
                <li>{country}</li>
            </ul>
        );
    }
}

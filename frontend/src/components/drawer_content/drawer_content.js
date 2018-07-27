import React from 'react';
import styled from 'styled-components';

export default class DrawerContent extends React.Component {
    render() {
        const {
            selectedRestroomData: { name, comment, street, city, country },
        } = this.props;

        //
        // TODO: Find resource for phone number. The API does not provide
        //

        return (
            <StyledUL>
                {!!name && (
                    <li>
                        <h3>Name:</h3>
                        <span>{name}</span>
                    </li>
                )}
                {!!comment && (
                    <li>
                        <h3>Comments:</h3>
                        <span>{comment}</span>
                    </li>
                )}
                {!!street && (
                    <li>
                        <h3>Street:</h3>
                        <span>{street}</span>
                    </li>
                )}
                {!!city && <li>{city}</li>}
                {!!country && <li>{country}</li>}
            </StyledUL>
        );
    }
}

const StyledUL = styled.ul`
    list-style-type: none;
    margin-left: 0;
    padding: 10px;
    max-width: 500px;

    li {
        margin-bottom: 5px;
    }
`;

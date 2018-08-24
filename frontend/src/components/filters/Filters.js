import React from 'react';
import './Filters.css';

const Filters = props => {
    return (
        <div className="filterbox">
            <div className="filter">
                <input
                    type="checkbox"
                    id="restrooms"
                    name="restrooms"
                    value="restrooms"
                    onChange={props.toggleRestrooms}
                    checked={props.restroomsChecked}
                />
                <label htmlFor="restrooms">Restrooms</label>
            </div>
            <div className="filter">
                <input
                    type="checkbox"
                    id="source2"
                    name="source2"
                    value="source2"
                />
                <label htmlFor="source2">Source 2</label>
            </div>
            <div className="filter">
                <input
                    type="checkbox"
                    id="source3"
                    name="source3"
                    value="source3"
                />
                <label htmlFor="source3">Source 3, etc...</label>
            </div>
        </div>
    );
};

export default Filters;

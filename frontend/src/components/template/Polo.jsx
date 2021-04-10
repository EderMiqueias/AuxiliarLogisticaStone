import React from 'react';

export default (props) => {

    const cardStyle = {
        borderColor: props.color
    }

    return (
        <div className="Card Polo" style={cardStyle}>
            <div className="Content">
                <h4>{props.base}</h4>
                <ul>
                    <li>Estoque: {props.estoque} terminais</li>
                    <li>Média diária: {props.average.toFixed(2)} terminais</li>
                </ul>
                <button className="button">Ordem de Expedição</button>
            </div>
        </div>
    );
}

import React from 'react';

import Polo from './Polo';
import Legend from './Legend'
import getAll from '../../services/polos'

export default (props) => {
    const polos = getAll().map((polo) => {
        return (
            <Polo
                base={polo.base}
                estoque={polo.estoque}
                average={polo.average}
                url={polo.url}
                color={getColorByStockDuration(polo.estoque, polo.average)}
            />
        );
    });

    return (
        <div>
            <div className="header">
                <h1 className="title">POLOS</h1><br/>
                <h4>Legenda:</h4>
                <Legend color="#42EC9A" text="COBERTURA IDEAL"/>
                <Legend color="#DFFF00" text="ATENÇÃO"/>
                <Legend color="#DE3163" text="PERIGO"/>
            </div>
            <div className="Polos">
                {polos}
            </div>
        </div>
    );
}

function getColorByStockDuration(estoque, media){
    let diasRestantes = estoque / media;

    // Cobertura Ideal
    if (diasRestantes >= 14 && diasRestantes <= 18){
        return "#42EC9A";
    }
    // Atenção
    else if (diasRestantes >= 10 && diasRestantes <= 23) {
        return "#DFFF00";
    }
    // Perigo
    else {
        return "#DE3163";
    }
}

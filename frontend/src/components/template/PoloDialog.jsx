import React from 'react';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';

import api from '../../services/api'

const PoloDialog = props => {
    const [open, setOpen] = React.useState(false);
    let nTerminals = props.ideal;

    const expedir = () => {
        let toSend = {
            data: { add_estoque: nTerminals }
        };
        api.post(`/polos/${props.url}`, toSend)
            .then((resp) => {
                if (resp.status === 200) {
                    fatherExpedir()
                }
            });
        handleClose();
    }

    const fatherExpedir = () => {
        props.childExpedir(nTerminals);
    }

    const handleChangeInput = (e) => {
        nTerminals = e.target.value;
    }

    const handleClickOpen = () => {
        setOpen(true);
    };

    const handleClose = () => {
        setOpen(false);
    };

    return (
        <div>
            <button className="button" onClick={handleClickOpen}>
                Ordem de Expedição
            </button>
            <Dialog open={open} onClose={handleClose} aria-labelledby="form-dialog-title">
                <DialogTitle id="form-dialog-title">{props.base}</DialogTitle>
                <DialogContent>
                    <DialogContentText>
                        Para uma cobertura ideal é recomendado o envio
                        de {props.ideal} terminais na próxima expedição.
                    </DialogContentText>
                    <TextField
                        autoFocus
                        id="nTerminals"
                        margin="dense"
                        label="Terminais à Expedir"
                        type="number"
                        fullWidth
                        required
                        defaultValue={props.ideal}
                        onChange={handleChangeInput}
                    />
                </DialogContent>
                <DialogActions>
                    <Button color="secondary" onClick={handleClose}>
                        Cancelar
                    </Button>
                    <Button color="primary" onClick={expedir}>
                        Enviar Expedição
                    </Button>
                </DialogActions>
            </Dialog>
        </div>
    );
}

export default PoloDialog;

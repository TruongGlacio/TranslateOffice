import React, { Fragment } from 'react';
import Typography from '@material-ui/core/Typography';
import TextField from '@material-ui/core/TextField';

const OutputLanguage = (props) => {
  return (
    <Fragment>
      <Typography variant='button' style={{fontWeight: 600}}>
        Translation
      </Typography>
      <TextField
        fullWidth
        multiline
        InputProps={{
          readOnly: true,
        }}
        rows={4}
        rowsMax={100}
        margin='normal'
        value={props.text}
        variant='outlined'
      />
    </Fragment>
  );
}

export default OutputLanguage;

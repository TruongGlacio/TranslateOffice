import React, { Fragment } from 'react';
import TextField from '@material-ui/core/TextField';
import Typography from '@material-ui/core/Typography';


 const InputLanguage = (props) => {

  const handleChange = (e) => {
    props.changeInput(e.target.value);
    console.log(e.target.value);
  }

  return (
    <Fragment>
      <Typography variant='button' style={{fontWeight: 600}}>
        Type here to translate your text ...
      </Typography>
      <TextField
        fullWidth
        autoFocus={true}
        rows={4}
        rowsMax={100}
        multiline
        margin='normal'
        onChange={handleChange}
        variant='outlined'
      />
    </Fragment>
  );
}

export default InputLanguage;

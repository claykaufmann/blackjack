import * as React from 'react';

const Card = (props) => {
  const data = props;
  const { value } = data;
  const { suit } = data;

  return (
    <>
      <p>
        Card value: {value}, card suit: {suit}
      </p>
    </>
  );
};

export default Card;

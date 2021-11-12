import * as React from 'react';

const Card = (props) => {
  const data = props;
  const { value, suit, visibility } = data;

  if (visibility === false) {
    return <p>backside of card</p>;
  }

  return (
    <>
      <p>
        {value} of {suit}
      </p>
    </>
  );
};

export default Card;

import React from 'react';
import Enzyme, { shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

Enzyme.configure({adapter: new Adapter()});

import Contact from '../Contact.react';

describe('Contact', () => {
  const contact = shallow(<Contact />);

  it('renders correctly', () => {
    expect(contact).toMatchSnapshot();
  });

  it('initializes name and telephone in state', () => {
    expect(contact.state()).toEqual({name: "", telephone: ""});
  });
});

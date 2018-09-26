import React from 'react';
import Enzyme, { shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

Enzyme.configure({adapter: new Adapter()});

import Contact from '../Contact.react';

describe('Contact', () => {
  const contact = shallow(<Contact />);

  beforeEach(() => {
    contact.setState({disable: true});
  });

  afterEach(() => {
    contact.setState({disable: true});
  })

  it('renders correctly', () => {
    expect(contact).toMatchSnapshot();
  });

  it('changes the disable status', () => {
    contact.instance().handleEditClick()

    expect(contact.instance().state.disable).toEqual(false)
  })
});

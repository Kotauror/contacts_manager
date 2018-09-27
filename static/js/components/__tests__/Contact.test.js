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

  it('changes the disable status when click on edit', () => {
    contact.instance().handleEdit()

    expect(contact.instance().state.disable).toEqual(false)
  })

  it('changes the disable status to true when click on save', () => {
    contact.instance().handleSave()

    expect(contact.instance().state.disable).toEqual(true)
  })

  it('clears temporary data in state after saving', () => {
    contact.setState({newName: "name", newTelephone: "1111"});
    contact.instance().handleSave()

    expect(contact.instance().state.newName).toEqual("")
    expect(contact.instance().state.newTelephone).toEqual("")
  })

});

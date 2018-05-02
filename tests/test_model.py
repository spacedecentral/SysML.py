import sysml
import pytest

@pytest.fixture
def model():
    "Create a SysML model instance"
    model = sysml.Model('USS Enterprise')
    return model

def test_elements(model):
    "Set and get model elements as a list of valid stereotypes"
    enterprise = sysml.Block('NCC-1701')
    saucersection = sysml.Block('Primary hull')
    model.elements = [enterprise, saucersection, sysml.Block('Secondary hull')]
    assert repr(enterprise) == "\xabblock\xbb 'NCC-1701'"
    assert repr(saucersection) == "\xabblock\xbb 'Primary hull'"
    assert repr(model.elements) == "[\xabblock\xbb 'NCC-1701', \xabblock\xbb 'Primary hull', \xabblock\xbb 'Secondary hull']"

def test_set_and_get_item(model):
    "Model elements should be assigned a unique id, and accessible as key-value pair, upon assimilation"
    enterprise = sysml.Block('NCC-1701')
    saucersection = sysml.Block('Primary hull')
    model["block-1"] = enterprise
    model["block-2"] = saucersection
    model["block-3"] = sysml.Block('Secondary hull')
    assert repr(model["block-1"]) == "\xabblock\xbb 'NCC-1701'"
    assert repr(model["block-2"]) == "\xabblock\xbb 'Primary hull'"
    assert repr(model["block-3"]) == "\xabblock\xbb 'Secondary hull'"

# @pytest.fixture
# def add_blocks(model):
#     "add block(s) to model using built-in 'add_block()' method"
#     enterprise = sysml.Block('NCC-1701')
#     saucersection = sysml.Block('Primary hull')
#     model.add_block(enterprise)
#     model.add_block(saucersection, sysml.Block('Secondary hull'))
#     return model
#
# def test_add_blocks(add_blocks):
#     assert repr(model.elements) == "[\xabblock\xbb 'NCC-1701', \xabblock\xbb 'Primary hull', \xabblock\xbb 'Secondary hull']"
#
# @pytest.fixture
# def create_relationships(add_blocks):
#     "Define relationships between model elements as a list of edges"
#     model.add_relationship(source = model.block['NCC-1701'], target = [saucersection, model.block['Secondary hull']], stereotype='composition')
#     return model

"""
def test_block_parts(add_block_relationships):
    assert repr(model.block['NCC-1701'].parts) == "[\xabblock\xbb 'Primary hull', \xabblock\xbb 'Secondary hull']"

def test_block_values(model):
    valueProperty = {'class':'Constitution','P/N':'NCC-1701'}
    model.block['USS Enterprise'].add_values(valueProperty)
    assert model.block['USS Enterprise'].values == {'P/N': 'NCC-1701', 'class': 'Constitution'}

def test_block_references():
    model = sysml.BlockDefinitionDiagram('warp drive model')
    model.new_block('antimatter')
    model.new_block('antimatter injector')
    model.new_block('dilithium crystal chamber')
    model.new_block(label='warp core', parts=[model.block['antimatter injector'], model.block['dilithium crystal chamber']]
                    #,
                    #flowProperties={'in':{'inflow':'antimatter'}, 'out':{'outflow':'power'}},
                    #references=model.block['antimatter']
                    )
    model.block['warp core'].add_references(model.block['antimatter'])
    assert repr(model.block['warp core'].references) == "[\xabblock\xbb 'antimatter']"

def test_block_flowProperties():
    model = sysml.BlockDefinitionDiagram('warp drive model')
    model.new_block('antimatter')
    model.new_block('antimatter injector')
    model.new_block('dilithium crystal chamber')
    model.new_block(label='warp core', parts=[model.block['antimatter injector'], model.block['dilithium crystal chamber']]
                    #,
                    #flowProperties={'in':{'inflow':'antimatter'}, 'out':{'outflow':'power'}},
                    #references=model.block['antimatter']
                    )
    model.block['warp core'].add_flowProperties({'in':{'inflow':'antimatter'}, 'out':{'outflow':'power'}})
    assert model.block['warp core'].flowProperties == {'in':{'inflow':'antimatter'}, 'out':{'outflow':'power'}}
"""
# bz_auto_verification

Plan : 
capabilities skeleton: 
- get verification command from bz comment

- how to get running job variables into the tool?
solution: run from command line with available job args. 

- get main dfg fot this bug and compare with current job

- check verification deployment env var 

- run it on undercloud : ?using python shell then ansible playbook ? 

- get correct passed/failed outcome

- handle auto bug verification &|| mail to the qe recipient

Flow: 
execute after tests : 
stage that executes the tool : 
python tool --verification-product: openstack (insinuates infrared usage the following options) --verification-topology :cont2_comp2 --verification-dfg: pidone
the tool will then executes the verification command from the undercloud (unless stated otherwise by an option ? ).

Abstraction:
Between different tool modules : 
 bz_comments,verification execution,bz_update,mail.   
 
 ?how to handle different verification methods?
 
 openstack=ir plugin
 rhev,openshift
 
 solution : check bug for product ,i,e.
 bz1647991 -> openstack, then use Infrared verification method.
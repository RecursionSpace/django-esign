# django-esign

Process electronic/digital signatures from people.

_django-esign is a tool to aid in compliance, you should consult with an attorney to independently validate that you legal obligations are being meet when it comes ot electronics/digital signatures._

https://www.govinfo.gov/content/pkg/PLAW-106publ229/pdf/PLAW-106publ229.pdf

## E-Sign Act
The requirements set forth by the [E-Sign Act](https://www.fdic.gov/regulations/compliance/manual/10/X-3.1.pdf) are used as a guideline for the feature set django-esign attempts to provide. The following excerpts are the programatical elements, the ones checked off have been added.
- [ ]  Prior Consent, Notice of Availability of Paper Records
- [ ]  Hardware and Software Requirements; Notice of Changes
- [ ]  Record Retention

# Database Models

The models provided serve to both aid in the storage of the consented information as well as validated the consentment process.

**informed_consumer_record_access** - Confirms that you have provided the consumer with information on how they can access the records, after agreement, and any limitations (your policies) on accessing the records.

**informed_consumer_agreement_duration** - Confirms that you have informed the consumer of the duration of the agreement (trasactional or relastionshional).

**consumer_affirmatively_consented** - The final validation, only true if all previous validations have been passed.

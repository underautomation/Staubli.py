## Licensing

- Updated `LicenseInfo` initialization logic for single-file apps by disabling process-based executable creation-date probing.
- Added `IsLicensed` property to expose a direct boolean check for `Licensed`, `Trial`, and `ExtraTrial` states.

## SOAP Data Model Improvements

- Added `ToString()` overrides for:
  - `AnthroConfig`
  - `ScaraConfig`
  - `VrbxConfig`
  - `Config`
- Enriched XML/API documentation comments in `MotionDesc` properties to improve readability and generated docs quality.

## SOAP V3 Response Updates

- Added `ToString()` overrides for response models:
  - `ForwardKinResponse`
  - `MoveJJResponse`
  - `ResetMotionResponse`
  - `ReverseKinResponse`
  - `SetPowerResponse`
- Refined `ResetMotionResponse` serialization contract:
  - XML root changed to `motionResponse`
  - response field renamed to `ReturnCode`
  - explicit XML element name set to `motRet`

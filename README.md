LongestCocoa
============

Programmers who write Objective-C must **REALLY** love its descriptive and verbose naming style. 

SoWhatAreTheLongestMethodOrConstantNamesInCocoaFramework? Here are some superb ones:

* outputImageProviderFromBufferWithPixelFormat:pixelsWide:pixelsHigh:baseAddress:bytesPerRow:releaseCallback:releaseContext:colorSpace:shouldColorMatch:
* kCMSampleBufferConduitNotificationParameter_UpcomingOutputPTSRangeMayOverlapQueuedOutputPTSRange

Run `python longest.py` to discover the first 10 longest names for each identifier type. Below is the output from `python longest.py iphoneos` and `python longest.py macosx`.

Compiled using Xcode 8.2.1 (8C1002)


Longest Names For iPhoneOS arm64 (iOS 10.2)
================

Longest Objective-C Interface Names
----------------
* [64] INGetAvailableRestaurantReservationBookingDefaultsIntentResponse
* [59] INGetUserCurrentRestaurantReservationBookingsIntentResponse
* [57] INGetAvailableRestaurantReservationBookingsIntentResponse
* [56] INGetAvailableRestaurantReservationBookingDefaultsIntent
* [51] INGetUserCurrentRestaurantReservationBookingsIntent
* [50] AVCaptureManualExposureBracketedStillImageSettings
* [49] INGetAvailableRestaurantReservationBookingsIntent
* [48] AVCaptureAutoExposureBracketedStillImageSettings
* [47] AVAssetResourceLoadingContentInformationRequest
* [47] MTLRenderPipelineColorAttachmentDescriptorArray

Longest Objective-C Protocol Names
----------------
* [64] INGetAvailableRestaurantReservationBookingDefaultsIntentHandling
* [59] INGetUserCurrentRestaurantReservationBookingsIntentHandling
* [57] INGetAvailableRestaurantReservationBookingsIntentHandling
* [44] GKFriendRequestComposeViewControllerDelegate
* [44] PKPaymentAuthorizationViewControllerDelegate
* [44] AVCaptureAudioDataOutputSampleBufferDelegate
* [44] UIViewControllerTransitionCoordinatorContext
* [44] AVCaptureVideoDataOutputSampleBufferDelegate
* [43] GKTurnBasedMatchmakerViewControllerDelegate
* [42] ABPeoplePickerNavigationControllerDelegate

Longest Objective-C Property Names
----------------
* [56] automaticallyEnablesStillImageStabilizationWhenAvailable
* [54] availableMediaCharacteristicsWithMediaSelectionOptions
* [49] lockingWhiteBalanceWithCustomDeviceGainsSupported
* [49] canUseNetworkResourcesForLiveStreamingWhilePaused
* [49] outputObscuredDueToInsufficientExternalProtection
* [49] previewingGestureRecognizerForFailureRelationship
* [48] automaticallyConfiguresCaptureDeviceForWideColor
* [48] lensStabilizationDuringBracketedCaptureSupported
* [47] usesExternalPlaybackWhileExternalScreenIsActive
* [47] threadGroupSizeIsMultipleOfThreadExecutionWidth

Longest Objective-C Method Names
----------------
* [202] initWithEnableFan:enableAirConditioner:enableClimateControl:enableAutoMode:airCirculationMode:fanSpeedIndex:fanSpeedPercentage:relativeFanSpeedSetting:temperature:relativeTemperatureSetting:climateZone:
* [162] drawIndexedPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:instanceCount:baseInstance:
* [149] drawIndexedPatches:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:indirectBuffer:indirectBufferOffset:
* [147] copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:
* [147] copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:
* [139] copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:
* [139] copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:
* [133] generateAmbientOcclusionTextureWithSize:raysPerSample:attenuationFactor:objectsToConsider:vertexAttributeNamed:materialPropertyNamed:
* [129] workoutWithActivityType:startDate:endDate:workoutEvents:totalEnergyBurned:totalDistance:totalSwimmingStrokeCount:device:metadata:
* [128] initRecurrenceWithFrequency:interval:daysOfTheWeek:daysOfTheMonth:monthsOfTheYear:weeksOfTheYear:daysOfTheYear:setPositions:end:

Longest Objective-C Method Names (0/1 Parameter)
----------------
* [71] recordsVideoOrientationAndMirroringChangesAsMetadataTrackForConnection:
* [70] automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers
* [70] playerViewControllerShouldAutomaticallyDismissAtPictureInPictureStart:
* [69] mediaSelectionCriteriaCanBeAppliedAutomaticallyToMediaSelectionGroup:
* [65] navigationControllerPreferredInterfaceOrientationForPresentation:
* [64] splitViewControllerPreferredInterfaceOrientationForPresentation:
* [63] pageViewControllerPreferredInterfaceOrientationForPresentation:
* [63] predicateForEvaluatingTriggerOccurringBeforeDateWithComponents:
* [63] requestAutomaticPassPresentationSuppressionWithResponseHandler:
* [62] predicateForEvaluatingTriggerOccurringAfterDateWithComponents:

Longest C Function Names
----------------
* [87] CMMetadataFormatDescriptionCreateWithMetadataFormatDescriptionAndMetadataSpecifications
* [86] CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionBlockBuffer
* [82] CMClosedCaptionFormatDescriptionCopyAsBigEndianClosedCaptionDescriptionBlockBuffer
* [79] CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionData
* [76] CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionBlockBuffer
* [76] CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionBlockBuffer
* [72] CMMetadataFormatDescriptionCopyAsBigEndianMetadataDescriptionBlockBuffer
* [72] CMTimeCodeFormatDescriptionCopyAsBigEndianTimeCodeDescriptionBlockBuffer
* [70] CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionBlockBuffer
* [70] CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionBlockBuffer

Longest Enum Names
----------------
* [68] INGetAvailableRestaurantReservationBookingDefaultsIntentResponseCode
* [63] INGetUserCurrentRestaurantReservationBookingsIntentResponseCode
* [55] HMCharacteristicValueCurrentHumidifierDehumidifierState
* [54] UNNotificationContentExtensionMediaPlayPauseButtonType
* [54] HMCharacteristicValueTargetHumidifierDehumidifierState
* [53] INGetAvailableRestaurantReservationBookingsIntentCode
* [50] HMCharacteristicValueCarbonMonoxideDetectionStatus
* [49] HMCharacteristicValueCarbonDioxideDetectionStatus
* [49] HMCharacteristicValueLockMechanismLastKnownAction
* [47] HMCharacteristicValueCurrentSecuritySystemState

Longest Enum Constant Names
----------------
* [93] kCMBufferQueueTrigger_WhenDurationBecomesGreaterThanOrEqualToAndBufferCountBecomesGreaterThan
* [91] INBookRestaurantReservationIntentCodeFailureRequiringAppLaunchServiceTemporarilyUnavailable
* [90] INGetUserCurrentRestaurantReservationBookingsIntentResponseCodeFailureRequestUnsatisfiable
* [89] INListRideOptionsIntentResponseCodeFailureRequiringAppLaunchServiceTemporarilyUnavailable
* [87] INListRideOptionsIntentResponseCodeFailureRequiringAppLaunchPreviousRideNeedsCompletion
* [87] INGetRideStatusIntentResponseCodeFailureRequiringAppLaunchServiceTemporarilyUnavailable
* [87] HMCharacteristicValueLockMechanismLastKnownActionUnsecuredUsingPhysicalMovementInterior
* [87] HMCharacteristicValueLockMechanismLastKnownActionUnsecuredUsingPhysicalMovementExterior
* [85] INRequestRideIntentResponseCodeFailureRequiringAppLaunchServiceTemporarilyUnavailable
* [85] HMCharacteristicValueLockMechanismLastKnownActionSecuredUsingPhysicalMovementInterior

Longest Variable Constant Names
----------------
* [96] kCMSampleBufferConduitNotificationParameter_UpcomingOutputPTSRangeMayOverlapQueuedOutputPTSRange
* [81] kCMTextMarkupAttribute_OrthogonalLinePositionPercentageRelativeToWritingDirection
* [78] kVTDecompressionPropertyKey_MinOutputPresentationTimeStampOfFramesBeingDecoded
* [78] kVTDecompressionPropertyKey_MaxOutputPresentationTimeStampOfFramesBeingDecoded
* [76] AVAssetResourceLoadingRequestStreamingContentKeyRequestRequiresPersistentKey
* [76] kCMMetadataFormatDescription_StructuralDependencyKey_DependencyIsInvalidFlag
* [74] MFMessageComposeViewControllerTextMessageAvailabilityDidChangeNotification
* [73] kCMMetadataFormatDescriptionMetadataSpecificationKey_StructuralDependency
* [72] kCMMetadataFormatDescriptionMetadataSpecificationKey_ExtendedLanguageTag
* [71] kCMTextMarkupAttribute_TextPositionPercentageRelativeToWritingDirection


Longest Names For MacOSX x86_64 (OS X 10.12)
================

Longest Objective-C Interface Names
----------------
* [50] TKSmartCardUserInteractionForSecurePINVerification
* [47] AVAssetResourceLoadingContentInformationRequest
* [47] MTLRenderPipelineColorAttachmentDescriptorArray
* [47] AVAudioEnvironmentDistanceAttenuationParameters
* [45] NSCollectionViewFlowLayoutInvalidationContext
* [44] IOBluetoothAccessibilityIgnoredTextFieldCell
* [44] TKSmartCardUserInteractionForSecurePINChange
* [43] ICScannerFunctionalUnitPositiveTransparency
* [43] ICScannerFunctionalUnitNegativeTransparency
* [43] MTLRenderPassColorAttachmentDescriptorArray

Longest Objective-C Protocol Names
----------------
* [49] IMServiceApplicationGroupListAuthorizationSupport
* [44] GKFriendRequestComposeViewControllerDelegate
* [44] IMServicePlugInGroupListHandlePictureSupport
* [44] AVCaptureAudioDataOutputSampleBufferDelegate
* [44] IMServicePlugInGroupListAuthorizationSupport
* [44] AVCaptureVideoDataOutputSampleBufferDelegate
* [43] IMServiceApplicationInstantMessagingSupport
* [43] GKTurnBasedMatchmakerViewControllerDelegate
* [42] NSSharingServicePickerTouchBarItemDelegate
* [41] AVPlayerItemMetadataCollectorPushDelegate

Longest Objective-C Property Names
----------------
* [54] availableMediaCharacteristicsWithMediaSelectionOptions
* [51] accessibilityDisplayShouldDifferentiateWithoutColor
* [49] canUseNetworkResourcesForLiveStreamingWhilePaused
* [49] outputObscuredDueToInsufficientExternalProtection
* [47] usesExternalPlaybackWhileExternalScreenIsActive
* [47] threadGroupSizeIsMultipleOfThreadExecutionWidth
* [46] maximumExtendedDynamicRangeColorComponentValue
* [46] automaticallyEnablesLowLightBoostWhenAvailable
* [45] requiredPixelBufferAttributesForRenderContext
* [44] fileNameExtensionWasHiddenInLastRunSavePanel

Longest Objective-C Method Names
----------------
* [162] drawIndexedPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:instanceCount:baseInstance:
* [150] outputImageProviderFromBufferWithPixelFormat:pixelsWide:pixelsHigh:baseAddress:bytesPerRow:releaseCallback:releaseContext:colorSpace:shouldColorMatch:
* [149] drawIndexedPatches:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:indirectBuffer:indirectBufferOffset:
* [148] initWithBitmapDataPlanes:pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bitmapFormat:bytesPerRow:bitsPerPixel:
* [147] copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:
* [147] copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:
* [140] outputImageProviderFromTextureWithPixelFormat:pixelsWide:pixelsHigh:name:flipped:releaseCallback:releaseContext:colorSpace:shouldColorMatch:
* [139] copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:
* [139] copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:
* [137] getLineFragmentRect:usedRect:remainingRect:forStartingGlyphAtIndex:proposedRect:lineSpacing:paragraphSpacingBefore:paragraphSpacingAfter:

Longest Objective-C Method Names (0/1 Parameter)
----------------
* [79] samplesWithEarlierDecodeTimeStampsMayHaveLaterPresentationTimeStampsThanCursor:
* [79] samplesWithLaterDecodeTimeStampsMayHaveEarlierPresentationTimeStampsThanCursor:
* [69] mediaSelectionCriteriaCanBeAppliedAutomaticallyToMediaSelectionGroup:
* [68] managedObjectContextsToMonitorWhenSyncingPersistentStoreCoordinator:
* [68] managedObjectContextsToReloadAfterSyncingPersistentStoreCoordinator:
* [59] generateIdentityVerificationSignatureWithCompletionHandler:
* [59] assetReaderOutputMetadataAdaptorWithAssetReaderTrackOutput:
* [58] conditionallyBeginAccessingResourcesWithCompletionHandler:
* [57] recommendedVideoSettingsForAssetWriterWithOutputFileType:
* [57] recommendedAudioSettingsForAssetWriterWithOutputFileType:

Longest C Function Names
----------------
* [87] CMMetadataFormatDescriptionCreateWithMetadataFormatDescriptionAndMetadataSpecifications
* [86] CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionBlockBuffer
* [82] CMClosedCaptionFormatDescriptionCopyAsBigEndianClosedCaptionDescriptionBlockBuffer
* [79] CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionData
* [76] CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionBlockBuffer
* [76] CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionBlockBuffer
* [72] CMMetadataFormatDescriptionCopyAsBigEndianMetadataDescriptionBlockBuffer
* [72] CMTimeCodeFormatDescriptionCopyAsBigEndianTimeCodeDescriptionBlockBuffer
* [70] CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionBlockBuffer
* [70] CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionBlockBuffer

Longest Enum Names
----------------
* [47] NSDateComponentsFormatterZeroFormattingBehavior
* [47] BluetoothLESecurityManagerKeyDistributionFormat
* [45] 'MTAudioProcessingTapCreationFlags':'unsigned
* [44] BluetoothHCIExtendedInquiryResponseDataTypes
* [44] AVCaptureDeviceTransportControlsPlaybackMode
* [43] IOBluetoothUserNotificationChannelDirection
* [43] NSTableViewDraggingDestinationFeedbackStyle
* [42] AVAudioEnvironmentDistanceAttenuationModel
* [41] BluetoothAuthenticationRequirementsValues
* [41] NSPersistentStoreUbiquitousTransitionType

Longest Enum Constant Names
----------------
* [93] kCMBufferQueueTrigger_WhenDurationBecomesGreaterThanOrEqualToAndBufferCountBecomesGreaterThan
* [88] kBluetoothAMPManagerCreatePhysicalLinkResponseAMPDisconnectedPhysicalLinkRequestReceived
* [84] kBluetoothLESecurityManagerReasonCodeCrossTransportKeyDerivationGenerationNotAllowed
* [84] kBluetoothHCIExtendedInquiryResponseDataType128BitServiceClassUUIDsWithMoreAvailable
* [83] kBluetoothHCIExtendedInquiryResponseDataType16BitServiceClassUUIDsWithMoreAvailable
* [83] kBluetoothHCIExtendedInquiryResponseDataType32BitServiceClassUUIDsWithMoreAvailable
* [79] kBluetoothHCIExtendedInquiryResponseDataType128BitServiceClassUUIDsCompleteList
* [78] kBluetoothHCIExtendedInquiryResponseDataType32BitServiceClassUUIDsCompleteList
* [78] kBluetoothHCIExtendedInquiryResponseDataTypeSecureConnectionsConfirmationValue
* [78] kBluetoothHCIExtendedInquiryResponseDataType16BitServiceClassUUIDsCompleteList

Longest Variable Constant Names
----------------
* [96] kCMSampleBufferConduitNotificationParameter_UpcomingOutputPTSRangeMayOverlapQueuedOutputPTSRange
* [81] kCMTextMarkupAttribute_OrthogonalLinePositionPercentageRelativeToWritingDirection
* [78] kVTDecompressionPropertyKey_MinOutputPresentationTimeStampOfFramesBeingDecoded
* [78] kVTDecompressionPropertyKey_MaxOutputPresentationTimeStampOfFramesBeingDecoded
* [76] AVAssetResourceLoadingRequestStreamingContentKeyRequestRequiresPersistentKey
* [76] kCMMetadataFormatDescription_StructuralDependencyKey_DependencyIsInvalidFlag
* [73] kCMMetadataFormatDescriptionMetadataSpecificationKey_StructuralDependency
* [72] kCMMetadataFormatDescriptionMetadataSpecificationKey_ExtendedLanguageTag
* [71] kCMTextMarkupAttribute_TextPositionPercentageRelativeToWritingDirection
* [69] kVTDecompressionPropertyKey_SupportedPixelFormatsOrderedByPerformance

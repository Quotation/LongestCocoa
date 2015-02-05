LongestCocoa
============

Programmers who write Objective-C must **REALLY** love its descriptive and verbose naming style. 

SoWhatAreTheLongestMethodOrConstantNamesInCocoaFramework? Here are some superb ones:

* outputImageProviderFromBufferWithPixelFormat:pixelsWide:pixelsHigh:baseAddress:bytesPerRow:releaseCallback:releaseContext:colorSpace:shouldColorMatch:
* kCMSampleBufferConduitNotificationParameter_UpcomingOutputPTSRangeMayOverlapQueuedOutputPTSRange

Run `python longest.py` to discover the first 10 longest names for each identifier type. Below is the output from `python longest.py iphoneos` and `python longest.py macosx`.

Compiled using Xcode 6.1.1 (6A2008a)

Longest Names For iPhoneOS armv7 (iOS 8.1)
================

Longest Objective-C Interface Names
----------------
* [50] AVCaptureManualExposureBracketedStillImageSettings
* [48] AVCaptureAutoExposureBracketedStillImageSettings
* [47] AVAudioEnvironmentDistanceAttenuationParameters
* [47] AVAssetResourceLoadingContentInformationRequest
* [47] MTLRenderPipelineColorAttachmentDescriptorArray
* [45] UICollectionViewFlowLayoutInvalidationContext
* [43] MTLRenderPassColorAttachmentDescriptorArray
* [42] MTLRenderPipelineColorAttachmentDescriptor
* [41] AVMutableVideoCompositionLayerInstruction
* [41] UICollectionViewLayoutInvalidationContext

Longest Objective-C Protocol Names
----------------
* [44] UIViewControllerTransitionCoordinatorContext
* [44] GKFriendRequestComposeViewControllerDelegate
* [44] AVCaptureAudioDataOutputSampleBufferDelegate
* [44] PKPaymentAuthorizationViewControllerDelegate
* [44] AVCaptureVideoDataOutputSampleBufferDelegate
* [43] GKTurnBasedMatchmakerViewControllerDelegate
* [42] ABPeoplePickerNavigationControllerDelegate
* [42] EAWiFiUnconfiguredAccessoryBrowserDelegate
* [40] UIAdaptivePresentationControllerDelegate
* [40] UIViewControllerInteractiveTransitioning

Longest Objective-C Property Names
----------------
* [56] automaticallyEnablesStillImageStabilizationWhenAvailable
* [54] availableMediaCharacteristicsWithMediaSelectionOptions
* [49] outputObscuredDueToInsufficientExternalProtection
* [47] usesExternalPlaybackWhileExternalScreenIsActive
* [46] automaticallyEnablesLowLightBoostWhenAvailable
* [46] automaticallyConfiguresApplicationAudioSession
* [45] requiredPixelBufferAttributesForRenderContext
* [44] modalPresentationCapturesStatusBarAppearance
* [43] canPerformMultiplePassesOverSourceMediaData
* [42] usesAirPlayVideoWhileAirPlayScreenIsActive

Longest Objective-C Method Names
----------------
* [139] copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:
* [139] copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:
* [128] initRecurrenceWithFrequency:interval:daysOfTheWeek:daysOfTheMonth:monthsOfTheYear:weeksOfTheYear:daysOfTheYear:setPositions:end:
* [126] copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:
* [120] geometrySourceWithData:semantic:vectorCount:floatComponents:componentsPerVector:bytesPerComponent:dataOffset:dataStride:
* [120] drawStrikethroughForGlyphRange:strikethroughType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:
* [115] layoutManager:boundingBoxForControlGlyphAtIndex:forTextContainer:proposedLineFragment:glyphPosition:characterIndex:
* [113] decimalNumberHandlerWithRoundingMode:scale:raiseOnExactness:raiseOnOverflow:raiseOnUnderflow:raiseOnDivideByZero:
* [112] drawUnderlineForGlyphRange:underlineType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:
* [111] getLineFragmentInsertionPointsForCharacterAtIndex:alternatePositions:inDisplayOrder:positions:characterIndexes:

Longest Objective-C Method Names (0/1 Parameter)
----------------
* [70] automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers
* [65] navigationControllerPreferredInterfaceOrientationForPresentation:
* [64] splitViewControllerPreferredInterfaceOrientationForPresentation:
* [63] pageViewControllerPreferredInterfaceOrientationForPresentation:
* [61] tabBarControllerPreferredInterfaceOrientationForPresentation:
* [60] backButtonBackgroundVerticalPositionAdjustmentForBarMetrics:
* [60] setAutomaticallyEnablesStillImageStabilizationWhenAvailable:
* [59] generateIdentityVerificationSignatureWithCompletionHandler:
* [59] assetReaderOutputMetadataAdaptorWithAssetReaderTrackOutput:
* [58] startSearchingForUnconfiguredAccessoriesMatchingPredicate:

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
* [46] EAWiFiUnconfiguredAccessoryConfigurationStatus
* [43] AVAudioSessionSilenceSecondaryAudioHintType
* [42] AVAudioEnvironmentDistanceAttenuationModel
* [41] NSPersistentStoreUbiquitousTransitionType
* [41] UIPageViewControllerNavigationOrientation
* [40] NSXMLParserExternalEntityResolvingPolicy
* [40] UIImagePickerControllerCameraCaptureMode
* [39] UIPageViewControllerNavigationDirection
* [39] HMCharacteristicValueLockMechanismState

Longest Enum Constant Names
----------------
* [87] HMCharacteristicValueLockMechanismLastKnownActionUnsecuredUsingPhysicalMovementInterior
* [87] HMCharacteristicValueLockMechanismLastKnownActionUnsecuredUsingPhysicalMovementExterior
* [85] HMCharacteristicValueLockMechanismLastKnownActionSecuredUsingPhysicalMovementInterior
* [85] HMCharacteristicValueLockMechanismLastKnownActionSecuredUsingPhysicalMovementExterior
* [82] HMCharacteristicValueLockMechanismLastKnownActionSecuredWithAutomaticSecureTimeout
* [72] EAWiFiUnconfiguredAccessoryConfigurationStatusUserCancelledConfiguration
* [68] HMCharacteristicValueLockMechanismLastKnownActionUnsecuredWithKeypad
* [66] HMCharacteristicValueLockMechanismLastKnownActionUnsecuredRemotely
* [66] kCMFormatDescriptionBridgeError_InvalidSerializedSampleDescription
* [66] kCMFormatDescriptionBridgeError_UnsupportedSampleDescriptionFlavor

Longest Variable Constant Names
----------------
* [96] kCMSampleBufferConduitNotificationParameter_UpcomingOutputPTSRangeMayOverlapQueuedOutputPTSRange
* [81] kCMTextMarkupAttribute_OrthogonalLinePositionPercentageRelativeToWritingDirection
* [78] kVTDecompressionPropertyKey_MinOutputPresentationTimeStampOfFramesBeingDecoded
* [78] kVTDecompressionPropertyKey_MaxOutputPresentationTimeStampOfFramesBeingDecoded
* [74] MFMessageComposeViewControllerTextMessageAvailabilityDidChangeNotification
* [72] kCMMetadataFormatDescriptionMetadataSpecificationKey_ExtendedLanguageTag
* [71] kCMTextMarkupAttribute_TextPositionPercentageRelativeToWritingDirection
* [69] kVTDecompressionPropertyKey_SupportedPixelFormatsOrderedByPerformance
* [68] kVTDecompressionPropertyKey_PixelFormatsWithReducedResolutionSupport
* [67] AVMetadataIdentifierID3MetadataOfficialInternetRadioStationHomepage

Longest Names For MacOSX x86_64 (OS X 10.10)
================

Longest Objective-C Interface Names
----------------
* [47] AVAssetResourceLoadingContentInformationRequest
* [43] ICScannerFunctionalUnitPositiveTransparency
* [43] ICScannerFunctionalUnitNegativeTransparency
* [41] AVMutableVideoCompositionLayerInstruction
* [37] ICScannerFunctionalUnitDocumentFeeder
* [37] AVAsynchronousVideoCompositionRequest
* [36] GKFriendRequestComposeViewController
* [36] AVMutableVideoCompositionInstruction
* [36] AVAssetWriterInputPixelBufferAdaptor
* [35] IOBluetoothDeviceSelectorController

Longest Objective-C Protocol Names
----------------
* [49] IMServiceApplicationGroupListAuthorizationSupport
* [44] GKFriendRequestComposeViewControllerDelegate
* [44] AVCaptureAudioDataOutputSampleBufferDelegate
* [44] IMServicePlugInGroupListAuthorizationSupport
* [44] AVCaptureVideoDataOutputSampleBufferDelegate
* [44] IMServicePlugInGroupListHandlePictureSupport
* [43] IMServiceApplicationInstantMessagingSupport
* [43] GKTurnBasedMatchmakerViewControllerDelegate
* [40] IOBluetoothHandsFreeAudioGatewayDelegate
* [39] IMServicePlugInGroupListOrderingSupport

Longest Objective-C Property Names
----------------
* [54] availableMediaCharacteristicsWithMediaSelectionOptions
* [46] automaticallyEnablesLowLightBoostWhenAvailable
* [45] requiredPixelBufferAttributesForRenderContext
* [42] appliesMediaSelectionCriteriaAutomatically
* [41] animatesToStartingPositionsOnCancelOrFail
* [40] incrementalSearchingShouldDimContentView
* [40] acceptsThresholdForBlackAndWhiteScanning
* [40] defaultThresholdForBlackAndWhiteScanning
* [40] seekingWaitsForVideoCompositionRendering
* [38] enablesVideoStabilizationWhenAvailable

Longest Objective-C Method Names
----------------
* [150] outputImageProviderFromBufferWithPixelFormat:pixelsWide:pixelsHigh:baseAddress:bytesPerRow:releaseCallback:releaseContext:colorSpace:shouldColorMatch:
* [148] initWithBitmapDataPlanes:pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bitmapFormat:bytesPerRow:bitsPerPixel:
* [140] outputImageProviderFromTextureWithPixelFormat:pixelsWide:pixelsHigh:name:flipped:releaseCallback:releaseContext:colorSpace:shouldColorMatch:
* [137] getLineFragmentRect:usedRect:remainingRect:forStartingGlyphAtIndex:proposedRect:lineSpacing:paragraphSpacingBefore:paragraphSpacingAfter:
* [135] initWithBitmapDataPlanes:pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bytesPerRow:bitsPerPixel:
* [133] initMouseEvent:canBubble:cancelable:view:detail:screenX:screenY:clientX:clientY:ctrlKey:altKey:shiftKey:metaKey:button:relatedTarget:
* [128] keyEventWithType:location:modifierFlags:timestamp:windowNumber:context:characters:charactersIgnoringModifiers:isARepeat:keyCode:
* [128] initRecurrenceWithFrequency:interval:daysOfTheWeek:daysOfTheMonth:monthsOfTheYear:weeksOfTheYear:daysOfTheYear:setPositions:end:
* [120] geometrySourceWithData:semantic:vectorCount:floatComponents:componentsPerVector:bytesPerComponent:dataOffset:dataStride:
* [120] drawStrikethroughForGlyphRange:strikethroughType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:

Longest Objective-C Method Names (0/1 Parameter)
----------------
* [68] managedObjectContextsToMonitorWhenSyncingPersistentStoreCoordinator:
* [68] managedObjectContextsToReloadAfterSyncingPersistentStoreCoordinator:
* [56] requestNotificationOfMediaDataChangeWithAdvanceInterval:
* [55] captureOutputShouldProvideSampleAccurateRecordingStart:
* [54] availableMediaCharacteristicsWithMediaSelectionOptions
* [54] startWirelessControllerDiscoveryWithCompletionHandler:
* [54] loadDefaultLeaderboardCategoryIDWithCompletionHandler:
* [54] accommodatePresentedItemDeletionWithCompletionHandler:
* [52] continueWithoutCredentialForAuthenticationChallenge:
* [52] selectMediaOptionAutomaticallyInMediaSelectionGroup:

Longest C Function Names
----------------
* [68] IOBluetoothOBEXSessionCreateWithIOBluetoothDeviceRefAndChannelNumber
* [64] IOBluetoothOBEXSessionCreateWithIncomingIOBluetoothRFCOMMChannel
* [63] CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback
* [63] IOBluetoothServiceBrowserControllerDiscoverWithDeviceAttributes
* [62] CVPixelFormatDescriptionRegisterDescriptionWithPixelFormatType
* [62] CMVideoFormatDescriptionGetExtensionKeysCommonWithImageBuffers
* [62] IOBluetoothOBEXSessionCreateWithIOBluetoothSDPServiceRecordRef
* [62] MACaptionAppearanceCopyPreferredCaptioningMediaCharacteristics
* [61] CFLocaleCreateCanonicalLocaleIdentifierFromScriptManagerCodes
* [60] IOBluetoothRegisterForFilteredRFCOMMChannelOpenNotifications

Longest Enum Names
----------------
* [47] BluetoothLESecurityManagerKeyDistributionFormat
* [44] BluetoothHCIExtendedInquiryResponseDataTypes
* [44] AVCaptureDeviceTransportControlsPlaybackMode
* [43] IOBluetoothUserNotificationChannelDirection
* [43] NSTableViewDraggingDestinationFeedbackStyle
* [41] NSPersistentStoreUbiquitousTransitionType
* [41] BluetoothAuthenticationRequirementsValues
* [40] NSXMLParserExternalEntityResolvingPolicy
* [39] BluetoothHCITransmitReadPowerLevelTypes
* [38] SDPAttributeDeviceIdentificationRecord

Longest Enum Constant Names
----------------
* [88] kBluetoothAMPManagerCreatePhysicalLinkResponseAMPDisconnectedPhysicalLinkRequestReceived
* [84] kBluetoothHCIExtendedInquiryResponseDataType128BitServiceClassUUIDsWithMoreAvailable
* [83] kBluetoothHCIExtendedInquiryResponseDataType32BitServiceClassUUIDsWithMoreAvailable
* [83] kBluetoothHCIExtendedInquiryResponseDataType16BitServiceClassUUIDsWithMoreAvailable
* [79] kBluetoothHCIExtendedInquiryResponseDataType128BitServiceClassUUIDsCompleteList
* [78] kBluetoothHCIExtendedInquiryResponseDataType32BitServiceClassUUIDsCompleteList
* [78] kBluetoothHCIExtendedInquiryResponseDataType16BitServiceClassUUIDsCompleteList
* [77] kBluetoothAuthenticationRequirementsMITMProtectionNotRequiredDedicatedBonding
* [75] kBluetoothAuthenticationRequirementsMITMProtectionNotRequiredGeneralBonding
* [74] kBluetoothHCIExtendedInquiryResponseDataTypeServiceSolicitation128BitUUIDs

Longest Variable Constant Names
----------------
* [96] kCMSampleBufferConduitNotificationParameter_UpcomingOutputPTSRangeMayOverlapQueuedOutputPTSRange
* [81] kCMTextMarkupAttribute_OrthogonalLinePositionPercentageRelativeToWritingDirection
* [78] kVTDecompressionPropertyKey_MaxOutputPresentationTimeStampOfFramesBeingDecoded
* [78] kVTDecompressionPropertyKey_MinOutputPresentationTimeStampOfFramesBeingDecoded
* [71] kCMTextMarkupAttribute_TextPositionPercentageRelativeToWritingDirection
* [69] kVTDecompressionPropertyKey_SupportedPixelFormatsOrderedByPerformance
* [68] kVTDecompressionPropertyKey_PixelFormatsWithReducedResolutionSupport
* [67] kVTVideoEncoderSpecification_RequireHardwareAcceleratedVideoEncoder
* [67] kVTVideoDecoderSpecification_RequireHardwareAcceleratedVideoDecoder
* [66] kVTVideoEncoderSpecification_EnableHardwareAcceleratedVideoEncoder
